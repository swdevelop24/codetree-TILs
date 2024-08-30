n=int(input())
for y in range(n):
    for x in range(n-y):
        print("*", end=" ")
    print()