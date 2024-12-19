a,b,c = tuple(map(int, input().split()))

def cal(*num):
    val = min(num)
    return val

print(cal(a,b,c))