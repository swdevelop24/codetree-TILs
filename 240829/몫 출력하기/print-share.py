t=0
while True:
    inp =int(input())
    if inp%2==0 and t<3:    
        print(inp//2) 
        t+=1
    if t>=3:
        break