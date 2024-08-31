n=int(input())

for y in range(1, n+1):
    for x in range(n):
        print(f"{y*n-x*y}", end=" ")
    print()