arr=list(map(int, input().split()))

cnt1=0
cnt2=0

for i in range(len(arr)):
    if i%2==0:
        cnt1+=arr[i]
    else:
        cnt2+=arr[i]

if cnt1 > cnt2:
    print(cnt1-cnt2)
else:
    print(cnt2-cnt1)