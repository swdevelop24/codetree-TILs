arr=input().split()
a,b,c=int(arr[0]), int(arr[1]),int(arr[2])

if a>b and a>c:
    if b>c:
        print(b)
    else:
        print(c)
elif b>a and b>c:
    if a>c:
        print(a)
    else:
        print(c)
elif c>a and c>b:
    if a<b:
        print(b)
    else:
        print(a)