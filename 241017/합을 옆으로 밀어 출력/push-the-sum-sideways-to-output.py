n=int(input())
total=0 
for _ in range(n):
    arr=int(input())
    total += arr

total = list(str(total))

temp = total[0]

for i in range(1,len(total)):
    total[i-1] = total[i] 

total[len(total)-1] = temp 

'''
# 문자열을 좌측으로 한 칸 밉기 
num_str = num_str[1:] + num_str[0]
'''

print(''.join(total))