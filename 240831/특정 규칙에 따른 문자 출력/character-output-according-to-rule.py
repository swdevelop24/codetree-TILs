n =int(input())

for i in range(n):
    for v in range(n-i-1):
        print(" ", end=' ')
    for x in range(i+1):
        print("@", end=' ')
    print()

for i in range(n-2, -1,-1):
    for x in range(i+1):
        print("@", end=' ')
    for v in range(n-i-1):
        print(" ", end='')
    print()