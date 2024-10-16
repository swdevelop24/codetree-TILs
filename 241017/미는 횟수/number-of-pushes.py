arr = input()
brr = input()

n = 0 

while True:
    # 회전:
    arr = list(arr)  # arr을 리스트로 변환
    temp = arr[-1]  
    for x in range(len(arr) - 1, 0,-1):
        arr[x] = arr[x - 1]  
    arr[0] = temp  # 첫 번째 문자를 마지막으로

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