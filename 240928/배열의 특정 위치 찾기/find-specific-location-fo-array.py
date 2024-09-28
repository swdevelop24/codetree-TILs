arr=list(map(int, input().split()))
sum_v=0
avg_v=0
sum_v=sum(arr[1::2])

total = arr[2::3]
cnt=len(total)
avg_v=sum(total)/cnt 

'''
for x in range(1, len(arr)):
    if x %3 ==0:
       total+=arr[x] 
       cnt+=1 

avg_v=total/cnt 
'''
print(f"{sum_v} {avg_v:.1f}")