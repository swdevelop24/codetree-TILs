import sys
mini=sys.maxsize
maxi = -sys.maxsize

arr=list(map(int, input().split()))

for num in arr:
    if num == 999 or num == -999:
        break
    if maxi < num:
        maxi = num
    if mini > num:
        mini= num


print(maxi, mini)