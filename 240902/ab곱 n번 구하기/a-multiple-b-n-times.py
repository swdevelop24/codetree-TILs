n=int(input())

for i in range(n):
    arr=input().split()
    a,b =int(arr[0]), int(arr[1])

    pro=1
    for x in range(a,b+1):
        pro*=x
    print(pro)