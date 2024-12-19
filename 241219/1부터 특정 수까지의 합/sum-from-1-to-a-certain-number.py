n=int(input())

def cal(n):
    val =0 
    for x in range(1, n+1):
        val+=x
    return val//10


print(cal(n))
