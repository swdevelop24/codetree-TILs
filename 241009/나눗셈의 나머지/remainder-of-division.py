n, r = input().split()
n = int(n)
r = int(r)

ret = 0
cnt = [0] * r
while n > 1:
    ret = n % r
    n = n // r
    cnt[ret] += 1

total = 0
for i in range(r):
    total += (cnt[i]) ** 2

print(total)