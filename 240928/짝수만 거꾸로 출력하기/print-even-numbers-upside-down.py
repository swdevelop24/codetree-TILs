n=int(input())
arr=list(map(int, input().split()))
my_list=[]
for x in arr:
    if x%2==0:
        my_list.append(x)

my_list.sort(reverse=True)

for num in my_list:
    print(num)