arr=input()

sum=0 
for elem in arr:
    if elem.isdigit():
        sum+=int(elem)

print(sum)