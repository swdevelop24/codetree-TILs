cl=0
hall=0
toil=0

n=int(input())
for num in range(n):
    if num%2==0:
        cl+=1
    if num%3==0:
        hall+=1
    if toil%12==0:
        toil+=1
    if num%2==0 and num%3==0 and toil%12!=0:
        cl-=1
        hall+=1
    if num%2==0 and num%3!=0 and toil%12==0:
        toil+=1
        cl-=1
    if num%2!=0 and num%3==0 and toil%12==0:
        toil+=1
        hall-=1
    if num%2==0 and num%3==0 and toil%12==0:
        toil+=1
        hall-=1
        cl-=1

print(cl, hall, toil, sep=' ')