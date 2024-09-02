n=int(input())

cnt='A'
for y in range(1,n+1):
    for x in range(y,0,-1):
        print(cnt, end='')
        cnt=chr(ord(cnt)+1)
    print()