'''
arr=input().split()
ret = arr[0].find(arr[1])
if ret == -1:
    print("No")
else:
    print(ret)
'''

string , a = tuple(input().split()) 
idx=-1 
length=len(string)

for i in range(length):
    if string[i] == a:
        idx = i 
        break

if idx ==-1:
    print("No")
else:
    print(idx)