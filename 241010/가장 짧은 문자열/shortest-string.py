a=input()
b=input()
c=input()

len1=len(a)
len2=len(b)
len3=len(c)

maxi = max(len1, len2, len3)
mini = min(len1, len2, len3)

print(maxi - mini)