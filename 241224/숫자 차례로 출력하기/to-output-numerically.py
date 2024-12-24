n=int(input())

def calc(n):

    if n==0:
        return

    calc(n-1)
    print(n, end=' ')

def calc2(n):
    if n==0:
        return
    
    print(n, end=' ')
    calc2(n-1)


calc(n)
print()
calc2(n)