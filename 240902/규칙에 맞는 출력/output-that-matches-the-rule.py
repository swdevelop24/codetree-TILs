n=int(input())

 
for y in range(n):
    cnt=n-y;
    for x in range(y+1):
        print(cnt, end=" ")
        cnt+=1
    print()