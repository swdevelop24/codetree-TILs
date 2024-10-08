arr=input().split()
a,b = int(arr[0]), int(arr[1])

newlist=[a,b]

for i in range(2,10):
    x = newlist[i-1]+ newlist[i-2]*2
    newlist.append(x)

for num in newlist:
    print(num, end=' ')