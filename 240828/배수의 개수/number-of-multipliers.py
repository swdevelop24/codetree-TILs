cnta=0
cntb=0

for _ in range(10):
    num=int(input())
    if num%3==0:
        cnta+=1
    if num%5==0:
        cntb+=1

print(cnta, cntb, sep=' ')