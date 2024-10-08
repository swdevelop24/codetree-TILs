n=int(input())

arr=list(map(int, input().split()))

cnt=0 
idx=0
for i, num in enumerate(arr):
    if num == 2:
        cnt+=1
    if cnt==3:
        idx =i 
        break

print(idx+1)