a,b = input(), input()
idx=-1 

alen=len(a)
blen=len(b)
cnt=0 

for i in range(alen):
    if a[i:i+blen] == b:
        idx = i 
        cnt+=1

if idx ==-1:
    print(0)
else:
    print(cnt)