n=int(input())

for y in range(n):
    for x in range(n):
        print(f"({n-y},{n-x})", end=" ")
    print()