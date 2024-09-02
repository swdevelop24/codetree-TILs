N = int(input())

cnt='A'
for y in range(N):
    for x in range(y):
        print(" ", end=" ")
    for t in range(N-y):
        print(cnt, end=" ")
        cnt=chr(ord(cnt)+1)
        if cnt>'Z':
            cnt='A'
    print()