import cv2 as cv
import numpy as np

path1 = 'img and vid/bolt_test_pothole.mp4'
path2 = 'img and vid/virat_test_pothole.mp4'

video1 = cv.VideoCapture(path2)

while True:

    ''' Reading images from video and converting to grayscale img '''
    isTrue, frame1 = video1.read()
    blank_img = np.zeros((frame1.shape[0], frame1.shape[1], 3), dtype='uint8')
    gray1 = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)


    ''' Threshold the original img to detect contours in later part '''
    ret, threshold1 = cv.threshold(gray1, 240, 255, cv.THRESH_BINARY)


    # Using mask for orange color detection :
    upper_bound = np.array([20, 255, 255])
    lower_bound = np.array([0, 100, 100])
    hsv_image = cv.cvtColor(frame1, cv.COLOR_BGR2HSV)
    mask_orange = cv.inRange(hsv_image, lower_bound, upper_bound)


    # removing noises from the mask images
    kernel = np.ones((3, 3), np.uint8)
    mask_orange = cv.morphologyEx(mask_orange, cv.MORPH_CLOSE, kernel)
    mask_orange = cv.morphologyEx(mask_orange, cv.MORPH_OPEN, kernel)


    # Applying contours to the 'mask_orange' img to highlight the obstacles
    contours_mask, _ = cv.findContours(mask_orange, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(frame1, contours_mask, -1, (200, 0, 0), 2)


    ''' using the threshold_img to find also the potholes by its shape and also drawing the contours on the img '''
    contours1, _ = cv.findContours(threshold1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for con in contours1:
        vertices1 = cv.approxPolyDP(con, 0.01 * cv.arcLength(con, True), True)
        vertices2 = cv.approxPolyDP(con, 0.01 * cv.arcLength(con, False), True)
        area = cv.contourArea(con)
        if 12 > len(vertices1) > 8 and 200 < cv.arcLength(con, True) < 600:
            # print(vertices1)
            cv.drawContours(frame1, [con], 0, (0, 255, 0), 3)

    # Showing the original img  with contours highlighted
    cv.imshow('contour_img', frame1)

    if cv.waitKey(10) and 0xFF == ord('d'):
        break

video1.release()
cv.destroyAllWindows()
cv.waitKey(0)
