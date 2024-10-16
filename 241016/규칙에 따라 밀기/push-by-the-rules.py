arr=input() 
order=input()

for x in range(len(order)):
    #shift to the left 
    if order[x] =='L':
        
        temp = arr[0]
        arr=arr[1:] + temp 
    

    else:
        temp = arr[-1]
        arr=temp + arr[:-1]
    

print(arr)