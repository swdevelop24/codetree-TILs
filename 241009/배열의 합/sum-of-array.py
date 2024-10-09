'''
for i in range(4):  
    arr=list(map(int, input().split()))
    print(sum(arr))
'''

# using list comprehension - again 
arr=[list(map(int, input().split())) for _ in range(4)]

for i in range(4):
    print(sum(arr[i]))