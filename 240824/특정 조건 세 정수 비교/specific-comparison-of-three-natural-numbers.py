arr=input().split()
a,b,c=int(arr[0]), int(arr[1]), int(arr[2])
d=0
if a<b and b<c:
    d=a
elif a>b and b<c:
    d=b
else:
    d=c

if a == d:
    print(1, end=" ")
else:
    print(0, end=" ")
if a==b and b==c:
    print(1, end=" ")
else:
    print(0, end=" ")