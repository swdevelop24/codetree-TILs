a, b = input().split() 
sub=0 
if ord(a) > ord(b):
    sub = ord(a)-ord(b)
else:
    sub = ord(b)-ord(a)

print(ord(a)+ord(b), sub)