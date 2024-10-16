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