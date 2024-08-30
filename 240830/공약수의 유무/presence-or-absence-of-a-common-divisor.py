arr=input().split()
a,b=int(arr[0]), int(arr[1])

flag=False
for num in range(a, b+1):
    if 1920%num ==0 and 2880%num==0:
        flag=True
        break

if flag:
    print(1)
else:
    print(0)