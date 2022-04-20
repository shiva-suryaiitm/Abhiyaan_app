# check for lowest among m and n
# using binary search

import math
dim = input(" Enter the dimension as row and columns : ").split()
dim = list(int(j) for j in dim)
k = int(input(" Enter the number need to find: "))
Mat = []
for i in range(int(dim[0])):                     # getting inputs here
    p = input(" ").split()
    p = list(int(j) for j in p)
    Mat.append(p)
# print(Mat)


maxi = max(dim)
mini = min(dim)              # getting min value of dim and its index value of min
index = dim.index(mini)
# print(mini)


row = []
for j in range(mini):
    if index == 0:
        k_index = [j,-1]
        
        if Mat[j][0] <= k <= Mat[j][maxi - 1]:    # concept here if the elemnts in matix are increasing ,
            row = Mat[j]                          # Then we can check if the element k presents by checking the last values of the row / column
            break
            
    if index == 1:
        
        if Mat[0][j] <= k <= Mat[maxi-1][j]:
            k_index = [-1, j]
            for g in range(maxi):
                row.append(Mat[g][j])
            break



if row != []:
    a, b,  c = 0, maxi-1, math.ceil((maxi-1)/2)
    T = 0
    while T < 1000:


        if row[math.ceil(c)] == k:
            print(f'The element {k} is found ')                 # binary search algorithm
            k_index[k_index.index(-1)] = c
            print(f'Index of the element is {k_index}')
            break

        if row[math.floor(c)] == k:
            print(f'The element {k} is found ')              # using math.ceil(c) and floor because it is not continuous
            k_index[k_index.index(-1)] = math.floor(c)
            print(f'Index of the element is {k_index}')      # As index num is not continuous so we are checking also the index
            break                                            # Here we considering the matrix is somewhat smaller 

        if row[math.ceil(c)] > k:
            b = math.ceil(c)
            c = (a+b)/2

        if row[math.ceil(c)] < k:
            a = math.ceil(c)
            c = (a+b)/2
        T += 0
    if T == 1000:
        print(" Sry element not found oops!...")
