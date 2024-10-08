import sys
n=int(input())
arr=list(map(int, input().split()))


cnt=0 
mini = sys.maxsize 
for num in arr:
    if mini > num:
        mini = num
        cnt=1
    elif mini== num:
        cnt+=1

print(mini, cnt)