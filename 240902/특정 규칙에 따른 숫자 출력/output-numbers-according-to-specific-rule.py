n=int(input())
cnt=1 

for y in range(n):
    for x in range(0,y):
        print(" ", end=" ")
    for _ in range(y,n):
        if cnt>9:
            cnt=1
        print(cnt,end=" ")
        cnt+=1
    print()