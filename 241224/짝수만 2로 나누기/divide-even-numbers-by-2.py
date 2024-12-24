n=int(input())
arr=list(map(int,input().split()))

for x in range(n):
    if arr[x] %2 ==0:
        print(arr[x]//2, end=' ')
    else:
        print(arr[x], end=' ')
