import sys
arr=list(map(int, input().split()))

maxi = -sys.maxsize

for num in arr:
    if num > maxi:
        maxi = num

print(maxi)