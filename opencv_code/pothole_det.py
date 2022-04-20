import cv2 as cv
import numpy as np

path1 = 'img and vid/bolt_test_pothole.mp4'
path2 = 'img and vid/virat_test_pothole.mp4'

video1 = cv.VideoCapture(path1)

while True:

    ''' Reading images from video and converting to grayscale img '''
    isTrue, frame1 = video1.read()
    gray1 = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)


    '''' Finding the threshold video and contours of threshold video '''
    _, threshold1 = cv.threshold(gray1, 200, 255, cv.THRESH_BINARY)
    contours1, _ = cv.findContours(threshold1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


    ''' Finding specific contours by its shape to find potholes and drawing it '''
    for con in contours1:
        vertices1 = cv.approxPolyDP(con, 0.01 * cv.arcLength(con, True), True)
        vertices2 = cv.approxPolyDP(con, 0.01 * cv.arcLength(con, False), True)
        if len(vertices1) > 9 and cv.arcLength(con, True) < 500 and len(vertices2) > 9:
            cv.drawContours(frame1, [con], 0, (0, 0, 255), 3)


    ''' showing original img with contours highlighted '''
    cv.imshow('contour_img', frame1)

    if cv.waitKey(10) and 0xFF == ord('d'):
        break

video1.release()
cv.destroyAllWindows()
cv.waitKey(0)
