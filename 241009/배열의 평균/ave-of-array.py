arr=[list(map(int, input().split())) for _ in range(2)]


for y in range(2):
    ravg=0
    ravg +=sum(arr[y]) 
    print(f"{ravg/4:.1f}", end=' ')
print()

for x in range(4):
    cavg=0
    for y in range(2):
        cavg+=arr[y][x]
    print(f"{cavg/2:.1f}", end=' ')
print()

tavg=0 
for y in range(2):
    for x in range(4):
        tavg+=arr[y][x]
print(f"{tavg/8:.1f}", end=' ')


'''

# 2차원 배열을 구현해 각 줄마다 정수를 입력받습니다.
arr_2d = [
	list(map(int, input().split()))
	for _ in range(2)
]

# 가로 평균
for i in range(2):
	sum_val = 0
	for j in range(4):
		sum_val += arr_2d[i][j]
	print(f"{sum_val / 4:.1f}", end=" ")
print()

# 세로 평균
for j in range(4):
	sum_val = 0
	for i in range(2):
		sum_val += arr_2d[i][j]
	print(f"{sum_val / 2:.1f}", end=" ")
print()

# 전체 평균
sum_val = 0
for i in range(4):
	for j in range(2):
		sum_val += arr_2d[j][i]
print(f"{sum_val / 8:.1f}")
'''