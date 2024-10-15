arr=input()
alen = len(arr) 

print(arr)
for x in range(alen):
    arr = arr[-1] + arr[0:-1]
    print(arr)