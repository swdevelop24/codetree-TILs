arr=input()
idx = arr.find('e')

arr = arr[:idx] + arr[idx+1:]
print(arr)


'''

# pop 함수를 사용하기 위해 문자열을 list로 전환
arr = list(string)
leng = len(arr)
	
# 문자열을 순회하며 e가 있는지 탐색
for i in range(leng):
    if arr[i] == 'e':
        # 해당 문자열이 e라면 그 원소를 제거
        arr.pop(i)
        leng -= 1
        break

# list를 문자열로 변환.
string = ''.join(arr)

# e가 제거된 문자열을 출력
print(string)
'''