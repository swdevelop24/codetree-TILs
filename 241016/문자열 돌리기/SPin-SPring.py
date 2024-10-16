arr=input() 
L=len(arr)

print(arr)
for x in range(L):
    arr=arr[-1]+arr[:L-1]
    print(arr)