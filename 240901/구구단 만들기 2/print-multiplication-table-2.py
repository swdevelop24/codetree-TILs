arr=input().split()
a,b=int(arr[0]), int(arr[1])


for y in range(2,9,2):
    for x in range(b,a-1,-1):
        print(f"{x} * {y} = {x*y} ", end="")
        if x!=a:
            print("/", end=" ")
    print()