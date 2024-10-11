n=int(input())
arr=[
    input()
    for _ in range(n)
]

ch = input()

cnt=0 
avg=0 
length=0
for elem in arr:
    if elem[0] == ch:
        cnt+=1 
        length+=len(elem)

avg = length/cnt

print(f"{cnt} {avg:.2f}")