flag = True
while flag:
    string = input()
    if string == 'END':
        flag=False
        break
    
    string=string[-1:0:-1] +string[0]

    print(string)


    '''
    # 문자열의 길이.
	leng = len(string)
		
	# 문자열을 역으로 출력.
	for i in range(leng - 1, -1, -1):
		print(string[i], end="")
	print()
    '''