arr=list(input())

first, second =arr[0] , arr[1]

for x in range(len(arr)): 
    if arr[x] == first:
        arr[x] = second
    elif arr[x] == second:
        arr[x] = first 

print(''.join(arr))