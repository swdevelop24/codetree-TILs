arr=[
    input()
    for _ in range(10)
]
ch = input()

flag=0
for elem in arr:
    if elem[len(elem)-1] == ch:
        print(elem)
        flag=1 

if not flag:
    print("None")