str1, str2 = tuple(input().split())
len1 = len(str1)
len2 =len(str2) 
if len1 == len2:
    print("same")

print(str1, len1) if len1 > len2 else print(str2, len2)