arr=input()
brr=input()

blen =len(brr)
while arr.find(brr) !=-1:
    idx  = arr.find(brr)
    if idx+blen > len(arr):
        break 
    arr= arr[:idx]+arr[idx+blen:]

print(arr)