arr=input().split()
a,b,c = int(arr[0]), int(arr[1]), int(arr[2])

ispro=False
for num in range(a,b+1):
    if num%c==0:
        ispro=True

if ispro:
    print("NO")
else:
    print("YES")