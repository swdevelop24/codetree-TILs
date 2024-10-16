arr=input()

sum=0 
for elem in arr:
    if elem.isdigit():
        sum+=int(elem)

print(sum)


'''
for elem in string:
    if ord(elem) >= ord('0') and ord(elem) <= ord('9'):
        ans += ord(elem) - ord('0')
'''