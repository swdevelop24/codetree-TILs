n=int(input())
arr=list(map(int, input().split()))
idx=n

preidx=n 
while True:
    max_idx=0 
    for i in range(1, preidx):
        if arr[i] > arr[max_idx]:
            max_idx=i

    print(max_idx+1, end=' ')

    if max_idx==0:
        break
    
    #직전 index 갱신
    preidx=max_idx