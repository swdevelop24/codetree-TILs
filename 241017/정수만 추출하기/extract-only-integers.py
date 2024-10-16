a, b = input().split() 

alast=0
blast=0 
for x in range(len(a)):
    if not a[x].isdigit():
        alast=x
        break


for x in range(len(b)):
    if not b[x].isdigit():
        blast=x
        break

sum1 = a[:alast]
sum2 =b[:blast]

print(int(sum1) + int(sum2))