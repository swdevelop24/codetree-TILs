arr=input()
brr=input()

n=0 

while True:
    arr=arr[1:-1] + arr[-1] + arr[0]
    n+=1 
    if arr == brr:
        break 
    if n == len(arr):
        n=-1
        break

print(n)