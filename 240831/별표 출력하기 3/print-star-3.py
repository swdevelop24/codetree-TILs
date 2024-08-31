n=int(input())

for y in range(n):
    for x in range(y):
        print(" ", end=" ")
    
    for t in range((2*n)-(2*y)-1):
        print("*", end=" ")
    print()