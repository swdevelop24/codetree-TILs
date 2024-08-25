inp = input().split() 
a=int(inp[0])
b=int(inp[1])

for i in range(a, b+1):
    if i %2 ==1:
        print(i, end=' ')