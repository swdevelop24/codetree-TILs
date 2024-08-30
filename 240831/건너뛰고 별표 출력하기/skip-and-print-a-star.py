n=int(input())


for y in range(n):
    for x in range(y+1):
        print("*", end="")
    print()
    print()

for y in range(n-2, -1,-1):
    for x in range(y+1):
        print("*", end="")
    print()
    print()