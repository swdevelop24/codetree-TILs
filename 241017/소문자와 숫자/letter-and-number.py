arr=input()

string =""
for elem in arr:
    if elem.isdigit():
        string+=elem
    if elem.isalpha():
        if elem >='A' and elem <='Z':
            string += chr(ord(elem)-ord('A')+ord('a'))
        else:
            string+=elem

print(string)


'''
for elem in string:
	if(elem >= 'A' and elem <= 'Z') or (elem >= 'a' and elem <= 'z'):
		print(elem.lower(), end="")
	
	if(elem >= '0' and elem <= '9'):
		print(elem, end="")
'''