points=list(map(int, input().split()))

for i in range(len(points)):
    if points[i] == 0:
        for x in range(i-1,-1,-1):
            print(points[x], end=" ")