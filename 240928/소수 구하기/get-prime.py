n = int(input())

for i in range(2,n+1):
    if n%i == 0:
        if i == n:
            print(i, end=' ') 
        else:
            continue
    else:
        print(i, end=' ')