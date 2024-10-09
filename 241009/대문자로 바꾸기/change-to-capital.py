arr=[list(input().split()) for _ in range(5)]

for y in range(5):
    for x in range(3):
        arr[y][x] = arr[y][x].upper() 

for y in range(5):
    for x in range(3):
        print(arr[y][x], end=' ')
    print()


''' 
아스키 코드 사용법
for i in range(5):
	for j in range(3):
		arr_2d[i][j] = chr(ord(arr_2d[i][j]) + ord('A') - ord('a'))
		print(arr_2d[i][j], end=" ")
	print()
'''