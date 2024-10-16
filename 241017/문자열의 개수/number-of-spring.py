flag=1
cnt=0
row=0
ret=[]
while flag:
    arr=input()
    row+=1
    if arr=='0':
        flag=1
        break
    if row %2 == 1:
        ret.append(arr) 
    cnt+=1 

print(cnt)
for elem in ret:
    print(elem)