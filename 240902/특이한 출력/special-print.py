n=int(input())

for y in range(1, n+1):
    for x in range(1, n+1):
        if (y+x) % 4 == 0:
            print(f"({y}, {x})")
        else:
            print(f"({y}, {x})", end=" ")