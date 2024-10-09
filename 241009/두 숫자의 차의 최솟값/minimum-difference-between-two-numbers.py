n=int(input())
arr=list(map(int,input().split()))

mini=100
for i in range(n):
    for x in range(i+1, n):
        if mini > arr[x] - arr[i]:
            mini = arr[x]-arr[i]

print(mini)