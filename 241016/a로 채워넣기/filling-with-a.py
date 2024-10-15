arr=list(input())

arr[1]='a'
arr[-2]='a'

print(''.join(arr))


'''
leng = len(string)

# 문자열의 앞에서 두 번째 원소와 뒤에서 두 번째 원소를 'a'로 대체합니다.
string = string[:1] + 'a' + string[2:]
string = string[:leng - 2] + 'a' + string[leng - 1:]
''