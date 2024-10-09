arr=[[0]*5 for _ in range(5)]  

for x in range(5):
    arr[0][x] =1 
    arr[x][0] =1 


for y in range(1,5):
    for x in range(1,5):
        arr[y][x] = arr[y-1][x] +arr[y][x-1]


for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()