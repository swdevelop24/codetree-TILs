arr, q =input().split()

q =int(q) 


for x in range(q):
    n = int(input())
    leng = len(arr)
    if n ==1:
        arr=arr[1:leng] + arr[0]
        print(arr)
    elif n == 2:
        arr= arr[-1]+arr[:leng-1]
        print(arr)
    else:
        arr=list(arr)
        left, right = int(0), int(leng-1)
        while left <=right:
            arr[left], arr[right] = arr[right], arr[left]
            left+=1
            right-=1
        print(''.join(arr))