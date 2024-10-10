n=int(input())

arr=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    arr[i][0]=1
    arr[0][i] =1 

for y in range(1, n):
    for x in range(1, n):
        arr[y][x] = arr[y-1][x-1] + arr[y-1][x] + arr[y][x-1]


for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()