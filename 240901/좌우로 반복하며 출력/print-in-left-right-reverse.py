n=int(input())

cnt=0
for y in range(n):
    for x in range(n): 
        if y%2==0:
            cnt+=1
            print(cnt,end='')
                  
        else:
            print(cnt, end='')
            cnt-=1
    print()