arr=list(map(int, input().split()))
cnt=[0]*10
i=0 
while True:
    tenth = arr[i]//10
    cnt[tenth]+=1
    if arr[i]==0:
        break
    i+=1


for i in range(1,10):
    print(f"{i} - {cnt[i]}")