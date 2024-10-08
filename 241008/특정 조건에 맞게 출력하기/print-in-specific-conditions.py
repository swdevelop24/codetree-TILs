arr=list(map(int, input().split()))

for num in arr:
    if num == 0:
        break
    if num %2 ==1:
        print(num+3, end=' ')
    else:
        print(num//2, end=' ')