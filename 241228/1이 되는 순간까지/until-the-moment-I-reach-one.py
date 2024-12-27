n=int(input())

def dfs(num):
    if num ==1:
        return 0

    if num %2 ==0:
        return dfs(num//2) +1
    else:
        return dfs(num//3) + 1  

print(dfs(n))