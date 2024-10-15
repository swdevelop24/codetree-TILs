s = input()
'''
s=list(s)
s.pop(1)
s.pop(-2)
print(''.join(s))
'''

s=s[:1]+s[2:]
s=s[:-2]+s[-1]
print(s)