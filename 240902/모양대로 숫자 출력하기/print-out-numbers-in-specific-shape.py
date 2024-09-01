n =int(input())

for y in range(n):
    for x in range(y):
        print(" ", end=" ")
    for t in range(n-y,0,-1):
        print(t, end=" ")
    print()