n =int(input())
arr=[[0 for _ in range(n)] for _ in range(n)]
num=1
for col in range(n-1, -1,-1):
    if col %2 == 1:
        for row in range(n-1,-1,-1):
            arr[row][col] = num 
            num +=1 

    else:
        for row in range(n):
            arr[row][col] = num 
            num +=1


for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()