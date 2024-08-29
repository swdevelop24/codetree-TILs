cnt=0
sum_v=0  
while True:
    age =int(input())
    if age>29 or age<20:
        break
    sum_v+=age
    cnt+=1


print(f"{sum_v/cnt:.2f}")