a, b =map(int, input().split())

sum = str(a+b)
cnt=0 
for elem in sum:
    if elem >='0' and elem <'9':
        if elem == '1':
            cnt+=1

print(cnt)