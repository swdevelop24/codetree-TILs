arr=input().split()
a,b=int(arr[0]), int(arr[1])

gop=1
for num in range(a,b+1):
    gop*=num

print(gop)