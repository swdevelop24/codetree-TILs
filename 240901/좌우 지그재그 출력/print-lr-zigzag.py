n=int(input())

for y in range(n):
    for x in range(n):
        if y%2==0:
            print((n*y)+x+1, end=' ')
        else:
            print((n*y)+n-x, end=" ")
    print()