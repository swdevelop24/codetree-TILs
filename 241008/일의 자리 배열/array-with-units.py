arr = input().split()
a,b = int(arr[0]), int(arr[1])

my_list=[a,b]

for i in range(3, 11):
    num = my_list[-1] + my_list[-2]
    num %=10
    my_list.append(num)

for x in my_list:
    print(x, end=' ')