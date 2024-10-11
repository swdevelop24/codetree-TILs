arr = input()
n =int(input())

num = len(arr)-1-n
if num < 0:
    num=1

for x in range(len(arr)-1,num, -1):
    print(arr[x], end='')