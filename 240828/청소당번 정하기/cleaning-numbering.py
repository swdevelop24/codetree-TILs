n=int(input())
cnt2, cnt3, cnt12=0,0,0

for num in range(1, n+1):
    if num%12==0:
        cnt12+=1
    elif num%3==0:
        cnt3+=1
    elif num%2==0:
        cnt2+=1

print(cnt2,cnt3, cnt12)