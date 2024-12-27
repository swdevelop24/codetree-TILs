n = int(input())

def dfs(num):
    if num ==0:
        return num
    
    return dfs(num-1) + num
 

print(dfs(n))