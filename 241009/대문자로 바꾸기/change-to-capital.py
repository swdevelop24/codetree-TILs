arr=[list(input().split()) for _ in range(5)]

for y in range(5):
    for x in range(3):
        arr[y][x] = arr[y][x].upper() 

for y in range(5):
    for x in range(3):
        print(arr[y][x], end=' ')
    print()