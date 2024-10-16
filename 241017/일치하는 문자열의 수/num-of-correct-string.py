n, string = input().split()
n =int(n)

cnt=0 
for _ in range(n) :
    test = input()
    if test == string:
        cnt +=1

print(cnt)