n=int(input())
arr=list(map(int, input().split()))
cnt=[0]*1001

for num in arr:
    cnt[num] +=1 

maxi=0
ex=0 
for i in range(n):
    if cnt[arr[i]] >=2:
        continue
    if maxi < arr[i]:
        maxi = arr[i]
        ex=0 
    else:
        ex=1 

if ex:
    print(-1)
else:
    print(maxi)