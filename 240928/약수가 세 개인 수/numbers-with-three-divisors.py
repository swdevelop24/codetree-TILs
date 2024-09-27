arr=input().split() 
start, end = int(arr[0]), int(arr[1])

cnt=0 
for i in range(start, end+1):
    num=0 
    for x in range(1,i+1): 
        if i%x ==0:
            num+=1
        
    if num == 3:
        cnt+=1

print(cnt)