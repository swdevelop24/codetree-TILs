arr=input().split()
a,b=int(arr[0]), int(arr[1])

gop=1

for num in range(1, b+1):
    if num%a==0:
        gop*=num

print(gop)