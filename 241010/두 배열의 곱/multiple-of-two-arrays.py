arr=[[1,2,3],[4,5,6],[7,8,9]]

brr=[[2,3,4],[5,6,7],[8,9,10]]

crr=[
    [0 for _ in range(3)]
    for _ in range(3)
] 

for y in range(3):
    for x in range(3):
        crr[y][x] = arr[y][x] * brr[y][x]


for row in crr:
    for ele in row:
        print(ele, end=' ')
    print()