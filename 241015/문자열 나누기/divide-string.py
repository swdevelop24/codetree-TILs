n =int(input())
arr=input().split() 

sum_char=''
for x in range(len(arr)): 
    sum_char+=''.join(arr[x])

row=0
for i in range(0,len(sum_char)):
   print(sum_char[i], end='')
   if (i+1)%5==0:
    print()