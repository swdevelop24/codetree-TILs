arr=input().split()
a=int(arr[0])
b=int(arr[1])

sum_value=0
for i in range(a, b+1):
    sum_value+=i

print(sum_value)