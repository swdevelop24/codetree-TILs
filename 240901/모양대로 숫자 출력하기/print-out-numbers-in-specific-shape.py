n =int(input())


for y in range(n):
    for x in range(n-y):
        for v in range(y):
            print(" ", end=" ")
        print(n-y-x, end=' ')
    print()