a,b = input(), input()
idx=-1 

alen=len(a)
blen=len(b)
cnt=0 

for i in range(alen-1):
    if a[i:i+2] == b:
        idx = i 
        cnt+=1

if idx ==-1:
    print(0)
else:
    print(cnt)