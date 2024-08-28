n=int(input())

sum_v=0 
for num in range(1, n):
    if n % num ==0:
        sum_v+=num

if sum_v==n:
    print("P")
else:
    print("N")