n, m =tuple(map(int, input().split()))
num=1
for y in range(n):
    for x in range(m):
        print(num, end=' ')
        num +=1 
    print()