n =int(input())

for y in range(n):
    for x in range(n-y):
        for i in range(n-y):
            print("*", end="")
        print(" ", end='')
    print()