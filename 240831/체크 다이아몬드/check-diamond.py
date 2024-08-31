n=int(input())

for y in range(n):
    for v in range(n-y-1):
        print(" ", end="")
    for x in range(y+1):
        print("*", end=" ")
    print()



for y in range(n-2,-1,-1):
    for v in range(n-y-1):
        print(" ", end="")
    for x in range(y+1):
        print("*", end=" ") 
    print()