n=int(input())

arr=[[0 for _ in range(n)] for _ in range(n)]

num=1 
for x in range(n):
    for y in range(n):
        arr[y][x] = num
        num +=1


for row in arr:
    for elem in row:
        print(elem, end= ' ')
    print()