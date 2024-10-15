arr=input()
idx = arr.find('e')

arr = arr[:idx] + arr[idx+1:]
print(arr)