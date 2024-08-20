# inp = input().split("-")
# n= inp[0]
# x=int(inp[1])
# y=int(inp[2])
# print(f"{n}-{y}-{x}")

# 가독성이 이게 더 좋음
# 변수 선언, 입력
inp = input()
arr = inp.split("-")
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

# 출력
print(f"010-{c}-{b}")