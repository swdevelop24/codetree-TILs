n=int(input())
arr=[1,n]
i=2 
while True:
    temp = arr[i-1]+arr[i-2]
    arr.append(temp)
    i+=1
    if temp > 100: 
        break 

for num in arr:
    print(num, end=' ')