n=int(input())


for y in range(n):
    for x in range(y+1):
        print("*", end=" ")
    print()

for  y in range(n):
    for x in range(n-1-y):
        print("*", end=" ")
    print()