arr=input()
brr=input()

blen =len(brr)
while arr.find(brr) !=-1:
    idx  = arr.find(brr)
    if idx+blen > len(arr):
        break 
    arr= arr[:idx]+arr[idx+blen:]

print(arr)


'''
while True:
    # a문자열에서 b문자열이 처음 등장하는 위치를 찾음 
    idx = -1
    
    # i, i+1, ..., i+len_b-1을 비교.
    # 이 때 마지막 위치는 i+len_b-1 < len_a를 만족해야
    # 하므로 i < len_a - len_b + 1을 구할 수 있음

    candidates = len_a - len_b + 1
    for i in range(candidates):
        # i부터 b길이만큼 비교
        is_same = True

        for j in range(len_b):
            if str_a[i + j] != str_b[j]:
                is_same = False
                break
        
        if is_same:
            # 문자열을 찾았으므로 i 반환
            idx = i
            break

    # 찾지 못한 경우
    if idx == -1:
        break
    
    # a문자열에서 idx위치에서 b문자열의 길이만큼의 문자를 지움 
    str_a = str_a[:idx] + str_a[idx + len_b:]

    len_a = len(str_a)

print(str_a)
'''