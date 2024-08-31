n=int(input())

for y in range(n):
    for x in range(n):
        if x%2==0: 
            print(y+1, end="")       
        else:
            print(n-y, end="")
    print()