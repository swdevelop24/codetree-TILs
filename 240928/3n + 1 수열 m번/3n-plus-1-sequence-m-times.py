m = int(input())


for i in range(m):
    n = int(input())
    complete = n 
    cnt=0
    sum=0  
    while n > 1: 
        if n%2 ==1:
            n = n*3 +1 
        else:
            n = n//2 
        cnt+=1
    print(cnt)