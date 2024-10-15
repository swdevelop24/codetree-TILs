arr=list(input()) 

fir = arr[0]
sec = arr[1]

for x in range(len(arr)):
    if arr[x] == sec:
        arr[x] = fir

print(''.join(arr))


'''
# 문자열을 순회하면서 두 번째 문자를 첫 번째 문자로 교환하는 방법.
for i in range(len(string)):
	if string[i] == b:
		string = string[:i] + a + string[i + 1:]
'''