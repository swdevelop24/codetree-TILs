a=input()

ret=""
for i in range(len(a)):
    if i%2==1:
        ret+=a[i]


for i in range(len(ret)-1,-1,-1):
    print(ret[i], end="")


#alternative
#idx = len(string) - 1
#if idx % 2 == 0: idx -= 1

# 문자열을 순회하여 조건대로 문자를 출력
#for i in range(idx, -1, -2):
#	print(string[i], end="")