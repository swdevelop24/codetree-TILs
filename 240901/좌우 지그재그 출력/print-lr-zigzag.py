n=int(input())

for y in range(n):
    for x in range(n):
        if y%2==0:
            print((y*n)+x+1, end=" ")
        else:
            print((y*n)+n-x, end=" ")
    print()