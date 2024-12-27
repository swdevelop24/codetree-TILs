n=int(input())

def dfs(num):
    if num ==0:
        return 
    
    print(num, end=' ')
    dfs(num-1)
    print(num, end=' ')

dfs(n)