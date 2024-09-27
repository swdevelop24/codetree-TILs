n = int(input())
for i in range(2, n+1): 
    isprime = True

    for x in range(2, i):
        if i % x == 0:
            isprime = False
    if isprime:
        print(i, end=" ")