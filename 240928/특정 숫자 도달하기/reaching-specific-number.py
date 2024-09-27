arr=list(map(int, input().split())) 

sum_v=0
cnt=0 
for elem in arr:
    if elem >=250:
        break
    sum_v += elem
    cnt+=1 
avg = sum_v/cnt 
print(f"{sum_v} {avg:.1f}")