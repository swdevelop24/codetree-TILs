n, m =tuple(map(int, input().split()))

arr=[[0]*(n+1) for _ in range(n+1)]

num=1 
for y in range(m):
    r, c = tuple(map(int, input().split()))
    arr[r][c]= num
    num+=1

for y in range(1,n+1):
    for x in range(1, n+1): 
        print(arr[y][x], end=' ')
    print()