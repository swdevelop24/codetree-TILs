n=int(input())

cnt=1
for y in range(n):
    for x in range(n):
        print(cnt, end='')
        if cnt< 9:
            cnt+=1
        else:
            cnt-=8

    
    print()