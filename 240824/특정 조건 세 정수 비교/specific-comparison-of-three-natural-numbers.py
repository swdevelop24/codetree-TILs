arr=input().split()
a,b,c=int(arr[0]), int(arr[1]), int(arr[2]) 
if a>=c and b>=c:
    mini=c
elif a>=b and c>=b:
    mini=b
else:
    mini =a 
if a == mini:
    print(1, end=" ")
else:
    print(0, end=" ")
if a==b and b==c:
    print(1, end=" ")
else:
    print(0, end=" ")