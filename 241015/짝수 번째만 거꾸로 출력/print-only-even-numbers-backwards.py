a=input()

ret=""
for i in range(len(a)):
    if i%2==1:
        ret+=a[i]


for i in range(len(ret)-1,-1,-1):
    print(ret[i], end="")