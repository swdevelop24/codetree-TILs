string, q = input().split()
q=int(q)

for x in range(q):
    arr = input().split()
    arr[0] =int(arr[0])
    if arr[0]==1:
        ath = int(arr[1])
        bth = int(arr[2])
        string = string[:ath] + string[bth] + string[ath+1:bth] + string[ath] + string[bth+1:]
    else:
        string=list(string)
        for x in range(len(string)):
            if string[x] == arr[1]:
                string[x] = arr[2] 
        string =''.join(string)
    print(string)