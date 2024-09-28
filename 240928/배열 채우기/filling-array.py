points=list(map(int, input().split()))

iszero=False
idx=0 
for i in range(len(points)):
    if points[i] == 0:
        iszero = True
        idx=i-1
        break
    

if iszero: 
    for x in range(idx, -1,-1):
        print(points[x], end=" ")
    
else:
    for x in range(len(points)-1,-1,-1):
        print(points[x], end=" ")