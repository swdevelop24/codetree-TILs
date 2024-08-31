n=int(input())

for i in range(n):
    for x in range(n-i):
        print("*", end="")
    for t in range(n, n+2*i):
        print(" ", end="")
    for x in range(n-i):
        print("*", end="")
    print()