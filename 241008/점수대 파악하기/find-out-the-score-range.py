arr=list(map(int, input().split()))

count=[0]*101
i=0
while True:
    if arr[i]==0:
        break
    temp = (arr[i]//10)*10
    count[temp]+=1
    i+=1 

for i in range(100, 0,-10):
    print(f"{i} - {count[i]}")