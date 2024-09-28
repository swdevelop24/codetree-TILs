arr=list(map(int, input().split()))
'''
sum_v=0
avg_v=0
sum_v=sum(arr[1::2])

total = arr[2::3]
cnt=len(total)
avg_v=sum(total)/cnt 

print(f"{sum_v} {avg_v:.1f}")
'''

sum_v=0
sum2=0 
cnt=0 

for i in range(10):
    if(i+1)%2 ==0:
        sum_v+=arr[i]
    if(i+1)%3 ==0:
        sum2+=arr[i] 
        cnt+=1
avg_v=sum2/cnt
print(f"{sum_v} {avg_v:.1f}")