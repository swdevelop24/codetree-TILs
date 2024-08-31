n=int(input())

for y in range(n*2+1):
    for x in range(n*2+1):
        if y == 0 or y==n-1 or x==0 or x==n-1 or (y%2 ==0) or (x%2==0):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()