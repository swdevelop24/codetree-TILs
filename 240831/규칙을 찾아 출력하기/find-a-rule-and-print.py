n=int(input())

for y in range(n):
    for x in range(n):
        if y==0 or x==0 or y==n-1 or x==n-1 or y>x:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()