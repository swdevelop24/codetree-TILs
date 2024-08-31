arr=input().split()
a=int(arr[0])
b=int(arr[1])

for y in range(1,a+1):
    for x in range(1,b+1):
        print(y*x, end=" ")
    print()