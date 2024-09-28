arr=list(map(int, input().split()))
sum_v=0
avg_v=0
sum_v=sum(arr[1::2])
cnt=0
total=0
for x in arr:
    if x %3 ==0:
       total+=x 
       cnt+=1 

avg_v=total/cnt 

print(f"{sum_v} {avg_v:.1f}")