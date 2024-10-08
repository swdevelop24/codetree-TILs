import sys
n=int(input())
arr=list(map(int, input().split()))


cnt=0 
mini = arr[0]
for num in range(1, n):
    if mini > num:
        mini = num
        cnt=1
    elif mini== num:
        cnt+=1

print(mini, cnt)