points=list(map(int, input().split()))
cnt=0 

for elem in points:
    if elem == 0:
        break
    cnt+=1

for i in range(cnt-1, -1, -1):
    print(points[i], end=' ')