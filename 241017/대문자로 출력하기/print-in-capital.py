arr=input()

string=""
for x in range(len(arr)):
    if (arr[x] >='A' and arr[x] <='Z') or (arr[x]>='a' and arr[x] <='z'):
        print(arr[x].upper(), end='')