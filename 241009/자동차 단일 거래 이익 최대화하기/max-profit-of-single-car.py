import sys 
n=int(input())
arr=list(map(int, input().split()))

max_profit=0
for i in range(n):
    for x in range(i+1, n):
        sum = arr[x] - arr[i]
        if max_profit < sum:
            max_profit = sum 
print(max_profit)