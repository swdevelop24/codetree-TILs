arr = input()
brr = input()

n = 0 

while True:
    # 회전: 첫 번째 문자를 마지막으로 이동
    arr = arr[1:] + arr[0]
    n += 1 
    
    # arr이 brr과 같아질 경우
    if arr == brr:
        break 
    
    # n이 len(arr)와 같아지면 회전을 중단
    if n == len(arr):
        n = -1
        break

print(n)