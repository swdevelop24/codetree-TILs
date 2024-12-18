n = int(input())

def rec(n):
    cnt=1
    for y in range(n):
        for x in range(n): 
            if cnt==10:
                cnt=1 
            print(cnt, end=' ')
            cnt+=1
        print()

rec(n)