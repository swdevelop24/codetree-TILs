a, b = input().split()

alast = 0
blast = 0

# 첫 번째 숫자가 아닌 문자의 위치 찾기
for x in range(len(a)):
    if not a[x].isdigit():
        alast = x
        break

for x in range(len(b)):
    if not b[x].isdigit():
        blast = x
        break

# 문자열의 앞 부분을 숫자로 변환하여 더하기
sum1 = a[:alast]
sum2 = b[:blast]

print(int(sum1) + int(sum2))