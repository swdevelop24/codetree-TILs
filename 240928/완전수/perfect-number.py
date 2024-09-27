arr = input().split() 
start, end = int(arr[0]) , int(arr[1]) 
cnt=0 
for i in range(start, end+1):
    sum=0
    for x in range(i-1,0,-1):
        if i % x  ==0: 
            sum += x 
    if sum == i:
        cnt+=1 
print(cnt)