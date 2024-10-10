a =input()
b =input()


arr=""
brr=""
for i in range(len(a)):
    if a[i] == " ":
        continue
    arr+="".join(a[i])

for i in range(len(b)):
    if b[i] == " ":
        continue
    brr+="".join(b[i])

print(arr+brr)