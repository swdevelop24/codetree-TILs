arr = input()
brr = input()

n = 0 

while True:
    # 회전: 첫 번째 문자를 마지막으로 이동
    arr = list(arr)  # arr을 리스트로 변환
    temp = arr[0]  # 첫 번째 문자 저장
    for x in range(len(arr) - 1):
        arr[x] = arr[x + 1]  # 각 문자를 왼쪽으로 이동
    arr[-1] = temp  # 첫 번째 문자를 마지막으로

    n += 1
    
    arr = ''.join(arr)  # 리스트를 문자열로 변환
    
    # arr이 brr과 같아질 경우
    if arr == brr:
        break 
    
    # n이 len(arr)과 같아지면 회전을 중단
    if n == len(arr)+1:
        n = -1
        break

print(n)