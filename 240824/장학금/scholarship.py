arr=input().split()
mid= int(arr[0])
end=int(arr[1])

if mid>90:
    if end>=95:
        print(100000)
    elif end>=90:
        print(50000)
    else:
        print(0)
else:
    print(0)