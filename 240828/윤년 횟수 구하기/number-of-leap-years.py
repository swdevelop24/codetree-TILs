n=int(input())
cnt=0
for yr in range(1,n+1):
    if yr%4==0:
        if yr%100==0 and yr%400!=0:
            pass
        else:
            cnt+=1
    
print(cnt)