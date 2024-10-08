n1,n2 = tuple(map(int, input().split()))

arr=list(map(int, input().split()))
brr=list(map(int, input().split()))

flag=0 
for b in range(n2):
    idx=0
    for a in arr:
        if b == a:
            idx = arr.index(a)
            break

    for i in range(idx,len(arr)-idx):
        if b !=arr[i]:
            flag=1
            break

if flag:
    print("No")

else:
    print("Yes")