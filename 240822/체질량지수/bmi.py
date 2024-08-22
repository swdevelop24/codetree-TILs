arr = input().split() 
h=int(arr[0])
w=int(arr[1])

b=(10000*w)/(h*h)

str="Obesity"    

if b>=25: 
    print(f"{int(b)}")
    print(str)
else: 
    print(f"{int(b)}")