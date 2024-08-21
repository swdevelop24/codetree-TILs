# 사칙연산 계산시 type은 더 큰 범위를 따라가게 되어있음
inp =input().split();
a = int(inp[0])
b=int(inp[1]) 
print(a+b)
print(a-b)
print(int(a//b))
print(int(a%b))