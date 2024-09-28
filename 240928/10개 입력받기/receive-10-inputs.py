arr=list(map(int, input().split())) 

cnt=0 
for i in range(len(arr)):
    if arr[i] == 0:
        break
    cnt+=1

sumv=0
avgv=0 
for x in range(cnt):
    sumv+=arr[x] 

avgv=sumv/cnt

print(f"{sumv} {avgv:.1f}")