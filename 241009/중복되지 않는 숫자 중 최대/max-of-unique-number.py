n=int(input())
arr=list(map(int, input().split()))
cnt=[0]*1001

for num in arr:
    cnt[num] +=1

maxi=-1

for i in range(n):
    if cnt[arr[i]] >= 2:
        continue
    if maxi < arr[i]:
        maxi = arr[i]

print(maxi if maxi !=-1 else -1)