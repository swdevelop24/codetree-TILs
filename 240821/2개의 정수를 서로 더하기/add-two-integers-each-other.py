# inp = input().split() 
# a =int(inp[0])
# b=int(inp[1])  
# a+=b
# b+=a

# print(f"{a} {b}")


# 변수 선언, 입력
inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

a += b
b += a

# 출력
print(a, b)