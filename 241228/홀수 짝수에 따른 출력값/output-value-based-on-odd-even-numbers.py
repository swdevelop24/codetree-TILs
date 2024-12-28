n=int(input())

def dfs(num):
    if num==1 or num ==2:
        return num
    
    if num%2 == 0:
        return dfs(num -2) + num
    
    else: 
        return dfs(num-2) + num 

print(dfs(n))

'''
def get_num(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    # n과 홀짝이 같은 수만을 재귀함수로 호출.
    return get_num(n - 2) + n


print(get_num(n))
'''