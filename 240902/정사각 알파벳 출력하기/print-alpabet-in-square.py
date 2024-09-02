n=int(input())

ch='A'
for y in range(1,n+1):
    for x in range(1,n+1):
        print(ch, end='')
        ch=chr(ord(ch)+1)
    print()