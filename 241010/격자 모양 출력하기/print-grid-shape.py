n, m = tuple(map(int, input().split()))

arr=[[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m): 
    r, c = tuple(map(int, input().split()))
    num = r*c 
    arr[r][c] = num 

for y in range(1, n+1):
    for x in range(1, n+1):
        print(arr[y][x], end=' ')
    print()