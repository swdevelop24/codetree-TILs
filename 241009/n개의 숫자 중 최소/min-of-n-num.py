import sys
n=int(input())
arr=list(map(int, input().split()))


cnt=0 
mini = arr[0]
for i in range(1, n):
    if mini > arr[i]:
        mini = arr[i]
        cnt=1
    elif mini== arr[i]:
        cnt+=1

print(mini, cnt)