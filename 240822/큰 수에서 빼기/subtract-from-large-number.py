arr=input().split()
a=int(arr[0])
b=int(arr[1])

big=0
small=0 

if a>b:
    big, small = a,b 
else:
    big, small = b,a 

print(big -small )