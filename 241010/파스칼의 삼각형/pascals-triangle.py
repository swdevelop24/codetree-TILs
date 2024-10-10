n=int(input())

arr=[[0]* n for _ in range(n)]

for i in range(n):
    arr[i][0] =1 

for y in range(1,n):
    for x in range(1,y+1):
        if arr[y-1][x] == 0:
            arr[y][x] =1 
        else:
            arr[y][x] =  arr[y-1][x] + arr[y-1][x-1]


for row in arr:
    for elem in row:
        if elem == 0:
            continue
        print(elem, end=' ')
    print()