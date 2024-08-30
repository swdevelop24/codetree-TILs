pro=True
for i in range(5):
    temp = int(input())
    if temp % 3!=0:
        pro=False
        break
    
if pro:
    print(1)
else:
    print(0)