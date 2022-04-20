import math
dim = input(" Enter the dimension as row and columns : ").split()
dim = list(int(j) for j in dim)
k = int(input(" Enter the number need to find: "))
Mat = []
for i in range(int(dim[0])):                     # getting inputs here
    p = input(" ").split()
    p = list(int(j) for j in p)
    Mat.append(p)
g = 1
for j in Mat:
    if k in j:
        g = 0
        print(f"Element found : {k} ")
        print(f" Element index : [{Mat.index(j)}][{j.index(k)}]")
if g == 1:
    print(f'Element not found : {k} ')
