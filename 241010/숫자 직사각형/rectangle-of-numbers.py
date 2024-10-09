n, m =tuple(map(int, input().split()))

arr=[
    [ 0 for _ in range(m)] 
    for _ in range(n)
]

num=1
for i in range(n):
    for x in range(m):
        arr[i][x]= num
        num+=1

for row in arr:
    for elem in row:
        print(elem, end=' ') 
    print()

'''
num=1
for y in range(n):
    for x in range(m):
        print(num, end=' ')
        num +=1 
    print()
'''