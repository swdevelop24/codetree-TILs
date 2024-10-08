cnt=[0]*5

for _ in range(3):
    a,b = input().split()
    b=int(b)

    if a == 'Y' and b>=37:
        type=1        
    elif a == 'N' and b>=37:
        type=2
    elif a=='Y' and b<37:
        type=3
    else:
        type=4
    cnt[type]+=1 

for i in range(1,5):
    print(cnt[i], end=' ')

if cnt[1] >=2:
    print('E')