'''
arr=list(input())

arr[1]='a'
arr[-2]='a'

print(''.join(arr))
'''

arr=input()
arr=arr[:1]+'a'+arr[2:-2]+'a'+arr[-1:]
print(arr)