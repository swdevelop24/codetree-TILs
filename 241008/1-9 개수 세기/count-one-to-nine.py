n=int(input())
arr=list(map(int, input().split()))
count=[0]*10

for num in arr:
    count[num]+=1 

for i in range(1,10):
    print(count[i])