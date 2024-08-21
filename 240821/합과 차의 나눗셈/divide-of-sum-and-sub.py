# arr =input().split()
# a=int(arr[0])
# b=int(arr[1])
# c = (a+b)/(a-b)
# print(f"{c:.2f}")

# 변수 선언 및 입력
inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

print(f"{(a + b) / (a - b):.2f}")