arr=input().split()
a,b =int(arr[0]), int(arr[1])

sum_v=0
s,e=0,0 
if b>a:
    s = a
    e = b
else:
    s=b
    e=a 
for num in range(s, e+1):
    if num%5==0:
        sum_v+=num

print(sum_v)