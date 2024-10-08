import sys
n=int(input())
arr=list(map(int, input().split()))

cnt=[0]*101 

mini = sys.maxsize 
for num in arr:
    if mini >= num:
        mini = num
        cnt[num]+=1

print(mini, cnt[mini])