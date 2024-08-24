a = input().split()
b=input().split()
c=input().split() 

asym =a[0]
at=int(a[1])

bs =b[0]
bt=int(b[1])

cs =c[0]
ct=int(c[1])

cnt=0
if asym =='Y' and at >=37:
    cnt+=1

if bs=='Y' and bt >=37:
    cnt+=1
if cs=='Y' and ct >=37:
    cnt+=1

if cnt>=2:
    print('E')
else:
    print('N')