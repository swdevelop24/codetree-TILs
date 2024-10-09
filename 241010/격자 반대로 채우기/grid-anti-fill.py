n = int(input())
arr = [[0] * n for _ in range(n)]
num = 1

det = 0
for col in range(n - 1, -1, -1):
    if det % 2 == 0: 
        for row in range(n - 1, -1, -1):
            arr[row][col] = num
            num += 1
    else:
        for row in range(n):
            arr[row][col] = num
            num += 1
    det+=1 

for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()

'''
 if (n - 1 - col) % 2 == 0:
        # 이 케이스에는 아래에서 위로 값을 채워줌
'''