n=int(input())
arr=list(map(int, input().split()))

new_arr=[print(x, end=' ') for x in arr if x%2==0]