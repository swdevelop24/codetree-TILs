arr = input()
n =int(input())

for x in range(len(arr)-1,len(arr)-1-n, -1):
    print(arr[x], end='')