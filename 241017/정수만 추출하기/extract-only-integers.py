a, b = input().split()

alast = len(a)
blast = len(b)

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

#에지 케이스에 유의하기 (전부다 디짓인 경우 )

'''
idx1 = 0
idx2 = 0

# a의 정수로 변환 가능한 최대 인덱스를 찾기
for elem in a:
	if elem <= '9' and elem >= '0':
		idx1 += 1
	else:
		break

# b의 정수로 변환 가능한 최대 인덱스를 찾기 .
for elem in b:
	if elem <= '9' and elem >= '0':
		idx2 += 1
	else:
		break
	
str1 = a[:idx1]
str2 = b[:idx2]
'''