arr=input().split()
a,b=int(arr[0]), int(arr[1])
if a >=1:
    for i in range(b):
        print(a, end='')
elif a <= 0:
    print(0)