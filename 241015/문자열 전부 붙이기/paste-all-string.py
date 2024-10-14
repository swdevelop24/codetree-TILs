n=int(input())

arr=""
for i in range(n):
    arr+=input()

print(arr)

'''
#diffrent method
string = [
	input()
	for _ in range(n)
]
str_all = ""

# 문자열을 전부 붙임
for i in range(n):
	str_all += string[i]
	
# 합쳐진 문자열을 출력
print(str_all)
'''