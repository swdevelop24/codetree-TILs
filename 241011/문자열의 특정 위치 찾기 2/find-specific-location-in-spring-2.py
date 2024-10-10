arr=["apple", "banana","grape", "blueberry", "orange"] 
ch = input()

cnt=0
for ele in arr:
   if ele[2] == ch or ele[3] ==ch:
        print(ele)
        cnt+=1
print(cnt)