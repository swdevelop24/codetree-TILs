arr=input().split()
a=int(arr[0])
b=int(arr[1])

for a in range(a,b+1):
    if a%2==1:
        print(a, end=' ')
        a*=2
        
    elif a%2==0:
        print(a, end=' ')
        a+=3