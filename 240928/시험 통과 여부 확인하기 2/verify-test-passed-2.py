n=int(input())
cnt=0
for i in range(n):
    sum_v=0
    arr=list(map(int,input().split()))
    sum_v = sum(arr)
    if sum_v/4 >=60:
        print("pass")
        cnt+=1
    else:
        print("fail")

print(cnt)