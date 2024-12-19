n = int(input()) 

def is_num(num):
    mul = num//10 + num%10
    if num % 2 == 0 and mul %5 ==0:
        return "Yes"
    else:
        return "No"

print(is_num(n))