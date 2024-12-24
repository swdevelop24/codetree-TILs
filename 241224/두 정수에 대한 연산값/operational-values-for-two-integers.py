a, b = map(int, input().split()) 

def calc(a,b):
    if a>b:
        a+=25
        b*=2
    else:
        b+=25
        a*=2 
    print(a,b)

calc(a,b)