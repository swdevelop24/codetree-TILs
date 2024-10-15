arr=input()
brr=input()

cnt=0
idx=0


while idx <len(arr):
    if arr[idx:].find(brr) == -1:
        cnt=0
        break
    else:
        cnt+=1
        idx = arr[idx:].find(brr)
        idx = idx+1

print(cnt)