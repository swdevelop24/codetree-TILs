n=int(input())

def dfs(num):
    if num == 1:
        return 2
    if num == 2:
        return 4
    
    return (dfs(num-1)*dfs(num-2)) %100


print(dfs(n))