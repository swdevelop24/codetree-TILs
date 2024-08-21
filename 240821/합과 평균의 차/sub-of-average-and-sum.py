# arr=input().split()
# a =int(arr[0])
# b =int(arr[1])
# c =int(arr[2])

# s = a+b+c
# a = s//3 
# print(s)
# print(a)
# print(s-a)


# 변수 선언, 입력
inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

# 출력
print(a + b + c)
print((a + b + c) // 3)
print((a + b + c) - (a + b + c) // 3)