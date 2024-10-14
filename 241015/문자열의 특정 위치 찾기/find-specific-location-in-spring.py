arr=input().split()
ret = arr[0].find(arr[1])
if ret == -1:
    print("No")
else:
    print(ret)