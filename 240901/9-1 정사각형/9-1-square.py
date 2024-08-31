n=int(input())

cnt=9 
for y in range(n):
    for x in range(n):
        print(cnt, end='')
        cnt-=1
        if cnt==0:
            cnt=9
    print()