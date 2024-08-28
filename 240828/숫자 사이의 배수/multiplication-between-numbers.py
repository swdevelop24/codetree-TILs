arr=input().split()
a,b=int(arr[0]), int(arr[1])

sum_v=0
avg_v=0
cnt=0 
for num in range(a,b+1):
    if num %5==0 or num%7==0:
        sum_v+=num
        cnt+=1 
avg_v=sum_v/cnt

print(f"{sum_v} {avg_v:.1f}")