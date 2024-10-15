# 입력 받기
string, q = input().split()
q = int(q)  # 쿼리 개수를 정수로 변환

# 각 쿼리 처리
for _ in range(q):
    arr = input().split()
    operation = int(arr[0])  # 쿼리 유형 (1: 교환, 2: 문자 대체)

    if operation == 1:
        ath = int(arr[1]) - 1  # 첫 번째 인덱스
        bth = int(arr[2]) - 1  # 두 번째 인덱스

        # 문자열을 리스트로 변환 후 인덱스의 문자 교환
        string = list(string)
        string[ath], string[bth] = string[bth], string[ath]
        string = ''.join(string)

    elif operation == 2:
        old_char = arr[1]  # 대체할 문자
        new_char = arr[2]  # 새로운 문자

        # 문자열을 리스트로 변환 후 문자 하나씩 치환
        string = list(string)
        for i in range(len(string)):
            if string[i] == old_char:
                string[i] = new_char
        string = ''.join(string)  # 다시 문자열로 변환

    # 쿼리 수행 후 결과 출력
    print(string)