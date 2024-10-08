n=int(input())
arr=list(map(int,input().split()))

arr=[print(arr[x]**2, end=" ") for x in range(n)]