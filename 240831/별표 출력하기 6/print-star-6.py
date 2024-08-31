n=int(input())


for y in range(n):
    for v in range(y):
        print(" ", end=" ")
    for x in range(n*2-2*y-1,0,-1):
        print("*", end=" ")
    print()


for y in range(n-2,-1,-1):
    for v in range(y):
        print(" ", end=" ")
    for x in range(n*2-2*y-1,0,-1):
        print("*", end=" ")
    print()