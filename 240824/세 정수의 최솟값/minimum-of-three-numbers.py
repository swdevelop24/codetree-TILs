arr=input().split()
a=int(arr[0])
b=int(arr[1])
c=int(arr[2])

if a<b and a<c:
    mini=a
elif b<a and b<c:
    mini=b
else:
    mini=c

print(mini)