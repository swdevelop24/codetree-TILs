n=int(input())
arr=list(map(int, input().split()))


def dfsmax(num):
    if num == 0:
        return arr[0]
    
    return max(dfsmax(num-1), arr[num])


print(dfsmax(n-1))

