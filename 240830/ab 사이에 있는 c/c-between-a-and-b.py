arr=input().split()
a=int(arr[0])
b=int(arr[1])
c=int(arr[2])
flag=False
for num in range(a,b+1):
    if num%c==0:
        flag=True
        break

if flag:
    print("YES")
else:
    print("NO")