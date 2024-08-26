arr=input().split()
a,b=int(arr[0]), int(arr[1])
if a>b:
    for a in range(a,b-1,-1):
        print(a, end=' ')
else:
    for b in range(b, a-1, -1):
        print(b, end=' ')