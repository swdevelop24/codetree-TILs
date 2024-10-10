n=int(input())

arr=[[0]* n for _ in range(n)]

for i in range(n):
    arr[i][0] =1 

for y in range(1,n):
    for x in range(1,y+1):
        if arr[y-1][x] == 0:
            arr[y][x] =1 
        else:
            arr[y][x] =  arr[y-1][x] + arr[y-1][x-1]

'''
	
# 배열의 각 행의 첫 열과 마지막 열을 1로 초기!! 요부분 잘 확인하기 
for i in range(n):
	arr[i][0] = 1
	arr[i][i] = 1
	
# 배열의 숫자를 채우기 이게 더 쉬움.. 
for i in range(n):
	for j in range(1, i):
		arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
'''


for row in arr:
    for elem in row:
        if elem == 0:
            continue
        print(elem, end=' ')
    print()