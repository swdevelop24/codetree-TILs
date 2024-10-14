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

'''
for i in range(0, leng - 1):
	if string[i] == 'e' and string[i + 1] == 'e':
		cnt1 += 1
	if string[i] == 'e' and string[i + 1] == 'b':
		cnt2 += 1
'''