arr=['L','E','B','R','O','S']

c=input()

'''
for i, ch in enumerate(arr):
    if ch == c:
        print(i)

if c not in arr:
    print("None")
'''

if c not in arr:
    print("None")
else:
    print(arr.index(c))