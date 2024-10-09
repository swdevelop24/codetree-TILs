n, m = tuple(map(int, input().split()))

arr=[list(map(int, input().split())) for _  in range(n)]
brr=[list(map(int, input().split())) for _  in range(n)]

crr=[[0 for _ in range(m)] for _ in range(n)]

for y in range(n):
    for x in range(m):
        if arr[y][x] == brr[y][x]:
            crr[y][x] = 0
        else:
            crr[y][x] = 1 

for row in crr:
    for ele in row:
        print(ele, end=' ')
    print()