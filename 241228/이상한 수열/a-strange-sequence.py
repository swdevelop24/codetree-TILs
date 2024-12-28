n=int(input())

def dfs(num):
    if num==1:
        return 1
    
    if num==2:
        return 2

    return dfs(num//3) + dfs(num-1)


print(dfs(n))