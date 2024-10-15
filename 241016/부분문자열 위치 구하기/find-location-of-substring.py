arr=input()
tar =input()

idx =-1

idx = arr.find(tar)
print(idx)



'''
import sys

input_str = input()
target_str = input()

input_len, target_len = len(input_str), len(target_str)


for i in range(input_len):
    # input_str의 i 부터 i + target_len - 1까지의 원소가
    # target_len의 0부터 target_len - 1 까지의 원소와
    # 정확히 일치하는지 확인합니다.

    # 끝 원소인 i + target_len - 1 번째가
    # 존재하지 않는다면 비교를 하지 않음
    if i + target_len - 1 >= input_len:
        continue
    
    # 비교
    is_matched = True
    for j in range(target_len):
        if input_str[i + j] != target_str[j]:
            is_matched = False
    
    if is_matched:
         # 모든 문자에 대하여 매칭이 된 경우:
        print(i)
        sys.exit(0)

print(-1)
'''