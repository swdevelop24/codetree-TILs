arr=input()

alen = len(arr)

eecnt =0 
ebcnt =0 
for i in range(alen):
    if arr[i-1: i+1] == 'ee':
        eecnt+=1 

for i in range(alen):
    if arr[i-1: i+1] == 'eb':
        ebcnt+=1

print(eecnt, ebcnt)