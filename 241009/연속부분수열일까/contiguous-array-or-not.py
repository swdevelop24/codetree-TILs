n1,n2 = tuple(map(int, input().split()))

arr=list(map(int, input().split()))
brr=list(map(int, input().split()))

flag=1 
for a in arr:
    if brr[0] == a:
        idx = arr.index(a)
        break

t=1
for i in range(idx,len(arr)-idx):
    if brr[t] !=arr[i]:
        flag=0
        break
    t+=1 

if not flag:
    print("No")

else:
    print("Yes")