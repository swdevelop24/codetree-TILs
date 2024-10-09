arr=[list(map(int, input().split())) for _ in range(4)]

sum =0

for y in range(4):
    for x in range(y+1):
        sum += arr[y][x]

print(sum)