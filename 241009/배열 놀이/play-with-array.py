n, q =tuple(map(int, input().split()))
arr=list(map(int, input().split()))

for _ in range(q):
    type=list(map(int, input().split()))
    if type[0]==1:
        print(arr[type[1]-1])
    elif type[0]==2:
        if type[1] in arr:
            print(arr.index(type[1])+1)
        else:
            print(0)
            
    else:
        for i, num in enumerate(arr):
            if i >= type[1]-1 and i <=type[2]-1:
                print(num, end=' ')