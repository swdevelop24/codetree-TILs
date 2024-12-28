n =int(input())

def dfs(num):
    if num <=2:
        return num
    
    return dfs(num-1)*num 

print(dfs(n))