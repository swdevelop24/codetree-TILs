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