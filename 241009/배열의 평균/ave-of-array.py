arr=[list(map(int, input().split())) for _ in range(2)]


for y in range(2):
    ravg=0
    ravg +=sum(arr[y]) 
    print(f"{ravg/4:.1f}", end=' ')
print()

for x in range(4):
    cavg=0
    for y in range(2):
        cavg+=arr[y][x]
    print(f"{cavg/2:.1f}", end=' ')
print()

tavg=0 
for y in range(2):
    for x in range(4):
        tavg+=arr[y][x]
print(f"{tavg/8:.1f}", end=' ')