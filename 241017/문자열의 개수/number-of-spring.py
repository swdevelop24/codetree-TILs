flag=1
cnt=0
row=0
ret=[]
while flag:
    arr=input()
    row+=1
    if arr=='0':
        flag=1
        break
    if row %2 == 1:
        ret.append(arr) 
    cnt+=1 

print(cnt)
for elem in ret:
    print(elem)


'''
# 0이 나올때까지 반복
while True:
	# 문자열을 입력
	inp = input()
	string.append(inp)
		
	# 0이 나올 경우 while문을 빠져나옴
	if string[cnt] == "0":
		break
		
	cnt += 1
	
# 문자열의 개수를 출력
print(cnt)
	
# 홀수 번째 문자열을 출력
for i in range(0, cnt, 2):
	print(string[i])
'''