# 변수 선언, 입력
n = int(input())

# 출력
for i in range(1, n+1):
    //3의 배수이거나
	if i % 3 == 0:
		print("0", end=" ")
    
    //3,6,9중 하나를 포함하는 수라면 10으로 나눴을때 나머지가 3,6,9
	elif i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
		print("0", end=" ")
    //3,6,9중 하나를 포함하는 수라면 10으로 나눴을때 몫이 3,6,9
	elif i // 10 == 3 or i // 10 == 6 or i // 10 == 9:
		print("0", end=" ")
	else:
		print(i, end=" ")