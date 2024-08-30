n=int(input())
for y in range(n):
    for x in range(n, y, -1):
        print("*", end=" ")
    print()