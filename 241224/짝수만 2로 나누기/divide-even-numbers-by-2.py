n=int(input())
arr=list(map(int,input().split()))


def modify(arr): 
    for x in range(n):
        if arr[x] %2 ==0:
            arr[x]//=2 

modify(arr)
for elem in arr:
    print(elem, end=' ')
