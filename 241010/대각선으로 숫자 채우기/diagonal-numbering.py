n, m = tuple(map(int, input().split()))

arr=[[0 for _ in range(m)] for _ in range(n)]

num=1 

for start_col in range(m):
    curr_col = start_col
    curr_row = 0

    while curr_row < n and curr_col>=0:
        arr[curr_row][curr_col] = num
        num +=1
        curr_row +=1
        curr_col-=1 
    

for start_row in range(1, n):
    curr_row = start_row
    curr_col = m-1

    while curr_row < n and curr_col>=0:
        arr[curr_row][curr_col] = num 
        num+=1
        curr_row +=1
        curr_col -=1


for row in arr:
    for elem in row: 
        print(elem, end=' ')
    print()