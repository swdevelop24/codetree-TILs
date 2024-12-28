n=int(input())

def dfs(num):
    if num==1 or num ==2:
        return num
    
    if num%2 == 0:
        return dfs(num -2) + num
    
    else: 
        return dfs(num-2) + num 

print(dfs(n))