string = input()
ch = input()

cnt=0 
for i in range(len(string)):
    if string[i] == ch:
        cnt+=1
print(cnt)