flag = True
while flag:
    string = input()
    if string == 'END':
        flag=False
        break
    
    string=string[-1:0:-1] +string[0]
    print(string)