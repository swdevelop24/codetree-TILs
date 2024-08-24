arr=input().split()
brr=input().split()
a_age =int(arr[0])
a_s= arr[1]
b_age=int(brr[0])
b_s= brr[1]

if (a_age>=19 and a_s=='M') or (b_age>=19 and b_s=='M'):
    print(1)
else:
    print(0)