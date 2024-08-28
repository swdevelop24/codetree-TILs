n=int(input())
sum_v=0 
for num in range(1,n+1):
    sum_v+=num
    if sum_v>=n:
        print(num)
        break