arr=list(map(int,input().split()))

def dfs(num):
    if num <10:
        return num
    
    return dfs(num//10) + num % 10


gop=1
for x in arr:
    gop*=x

print(dfs(gop))