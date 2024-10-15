arr=list(input())

first, second =arr[0] , arr[1]

for x in range(len(arr)): 
    if arr[x] == first:
        arr[x] = second
    elif arr[x] == second:
        arr[x] = first 

print(''.join(arr)) 


'''
# 문자열을 순회하면서 첫 번째 문자와 두 번째 문자를 교환
for i in range(len(string)):
	if string[i] == a:
		string = string[:i] + b + string[i + 1:]
	elif string[i] == b:
		string = string[:i] + a + string[i + 1:]
'''