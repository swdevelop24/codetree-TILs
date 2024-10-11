arr=input().split()

cnt=0 
for ele in arr:
    for x in range(len(ele)):
        cnt+=1

print(cnt)