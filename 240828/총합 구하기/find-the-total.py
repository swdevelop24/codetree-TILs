arr=input().split()
a, b=int(arr[0]), int(arr[1])

sum_v=0
for num in range(a, b+1):
    if num%6 ==0  and num%8!=0:
       sum_v+=num

print(sum_v)