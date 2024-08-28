n=int(input())

sum_v=0
cnt=0

for _ in range(n):
    num=int(input())
    sum_v+=num

print(f"{sum_v} {sum_v/n:.1f}")