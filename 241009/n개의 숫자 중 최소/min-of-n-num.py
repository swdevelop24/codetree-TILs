import sys
n=int(input())
arr=list(map(int, input().split()))


cnt=1 
mini = arr[0]
for num in arr[1:]:
    if mini > num:
        mini = num
        cnt=1
    elif mini == num:
        cnt+=1

print(mini, cnt)