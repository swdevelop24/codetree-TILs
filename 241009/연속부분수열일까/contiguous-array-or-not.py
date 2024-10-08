import sys
n1, n2 = map(int, input().split())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

'''
flag = False
for i in range(n1 - n2 + 1):  # `arr`에서 `brr`를 검사할 수 있는 모든 시작 지점을 순회
    if arr[i:i+n2] == brr:    # `arr`의 부분 배열이 `brr`와 일치하는지 확인
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")
''' 


for i in range(n1):    
    flag=True
    for x in range(n2):
        if i+x >= n1:
            flag=False
            break

        if arr[i+x] != brr[x]:
            flag=False
            break
        
        
    if flag:
        print("Yes")
        sys.exit()

print("No")