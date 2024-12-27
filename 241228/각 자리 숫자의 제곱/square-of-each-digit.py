n=int(input())

def dfs(num):
    if num <10:
        return num*num
    
    return dfs(num//10)+((num%10)**2)

print(dfs(n))