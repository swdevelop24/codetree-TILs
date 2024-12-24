n, m = map(int, input().split())
arr = list(map(int,input().split()))

for _ in range(m):
    a, b = map(int, input().split())
    val=0 
    for x in range(a-1,b):
        val+=arr[x]
    print(val)