maxi=0
mini=1001

arr=list(map(int, input().split()))

for num in arr:
    if num <500 and maxi < num:
        maxi = num
    if num > 500 and mini > num:
        mini=num

print(maxi, mini)