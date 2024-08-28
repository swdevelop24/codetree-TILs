sum_v=0
avg_v=0
cnt=0 

for _ in range(10):
    num =int(input())
    if num >=0  and num<=200:
        sum_v+=num
        cnt+=1

avg_v=sum_v/cnt

print(f"{sum_v} {avg_v:.1f}")