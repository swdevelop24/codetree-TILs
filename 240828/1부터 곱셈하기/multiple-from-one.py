n=int(input())

pro=1
for num in range(1, 11):
    pro*=num
    if pro>=n:
        print(num)
        break