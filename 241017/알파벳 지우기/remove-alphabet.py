arr=input()
brr=input()
num1=""
num2="" 
for elem in arr:
	if elem.isalpha():
		continue
	else:
		num1+=elem


for elem in brr:
	if elem.isalpha():
		continue
	else:
		num2+=elem

print(int(num1)+int(num2))


'''
# a의 정수로 변환 가능한 부분을 다른 문자열로 옮김
for elem in a:
	if ord(elem) <= ord('9') and ord(elem) >= ord('0'):
		str1 += elem
	
# b의 정수로 변환 가능한 부분을 다른 문자열로 옮김 
for elem in b:
	if ord(elem) <= ord('9') and ord(elem) >= ord('0'):
		str2 += elem
'''