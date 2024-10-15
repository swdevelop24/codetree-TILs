string=input() 
slen = len(string)

string = list(string)
currlen=slen 
while currlen >1:
    idx = int(input())
    if idx >= currlen:
        string.pop(currlen-1)
    else:
        string.pop(idx)
    currlen = len(string)
    print(''.join(string))


'''
# 정수가 문자열의 길이 이상이면 마지막 문자를 가리키게 변경
	if a >= leng:
		a = leng - 1
		
	arr.pop(a)
	leng -= 1

	string = ''.join(arr)
'''