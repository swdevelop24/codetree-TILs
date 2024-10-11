arr = input()
n =int(input())

num = len(arr)
cnt=0 

# edge case 에 유의하기=> 몇개 인지 모르기 맨 마지막까지 순회!!! 
# 1개인 경우에 에러 날수 있음. 
for x in range(len(arr)-1,-1, -1):
    if cnt >=n:
        break
    print(arr[x], end=' ')
    cnt+=1