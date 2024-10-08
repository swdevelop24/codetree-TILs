n=int(input())
arr=[1,n]

num=0
i=2 
temp=arr[0]+arr[1] 
while temp <= 100:
    temp = arr[i-1]+arr[i-2]
    arr.append(temp)
    i+=1
    if temp > 100: 
        break 

for num in arr:
    print(num, end=' ')