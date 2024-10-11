n = int(input())
arr=[
    input()
    for _ in range(n)
]

cnt=0
cnta=0
for ele in arr:
    cnt+=len(ele)
    if ele[0] == 'a':
        cnta+=1

print(cnt, cnta)