arr = list(map(int, input().split()))
sum_v=0
cnt=0 

for num in arr:
    if num ==0:
        break
    if num %2 ==0:
        sum_v+= num
        cnt+=1 

print(cnt, sum_v)



'''
cnt=0 
for i in range(10):
    if arr[i] ==0:
        break
    cnt+=1 

sum_v=0 
cnt_v=0
for x in range(cnt):
    if arr[x] %2==0:
        sum_v+=arr[x]
        cnt_v+=1 
print(cnt_v, end=' ')
print(sum_v, end=' ')
'''