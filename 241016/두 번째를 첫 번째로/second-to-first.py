arr=list(input()) 

fir = arr[0]
sec = arr[1]

for x in range(len(arr)):
    if arr[x] == sec:
        arr[x] = fir

print(''.join(arr))