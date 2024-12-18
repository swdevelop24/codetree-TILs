n, m = map(int, input().split())

cnt=1 
left=1
right=1
for i in range(1, max(n, m)+1):
    if n % i == 0 and m % i == 0:
        cnt*=i
    

print(cnt)