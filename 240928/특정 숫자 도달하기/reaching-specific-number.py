arr=list(map(int, input().split())) 

above= False
idx =0  
for i in range(len(arr)):
    if arr[i] >= 250:
        above = True
        idx =i 
        break

my_sum=0
avg=0 
if above: 
    for i in range(idx):
        my_sum+=arr[i]
    avg = my_sum/idx
else:
    for idx in range(len(arr)-1):
        my_sum+=arr[idx]
    avg = my_sum/len(arr)

print(f"{my_sum} {avg:.1f}")