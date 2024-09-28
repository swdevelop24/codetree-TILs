n=int(input())
arr=list(map(int, input().split()))
for x in range(n-1,-1,-1):
    if arr[x]%2==0:
        print(arr[x], end=' ')