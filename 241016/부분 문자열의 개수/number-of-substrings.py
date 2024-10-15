a,b = input(), input()

alen=len(a)
blen=len(b)
cnt=0 

for i in range(alen-1):
    if a[i:i+2] == b:
        cnt+=1


print(cnt)