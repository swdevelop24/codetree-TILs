n, m =tuple(map(int, input().split()))

arr=[[0 for _ in range(m)] for _ in range(n)]

num=0 
for x in range(m):
    if x %2 ==0:
        for y in range(n):
            arr[y][x] = num
            num +=1 
    else:
        for y in range(n-1,-1,-1):
            arr[y][x] = num
            num+=1 


for row in arr:
    for ele in row:
        print(ele, end= ' ')
    print()

''' 
or 
for row in range(n):
    for col in range(m):
        print(answer[row][col], end = ' ')
    print()
'''