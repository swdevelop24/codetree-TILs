n = int(input())
arr=[
    input()
    for _ in range(n)
]

cnt=0
cnta=0
for ele in arr:
    cnt+=len(ele)
    for x in range(len(ele)):
        if ele[x] == 'a':
            cnta+=1

print(cnt, cnta)