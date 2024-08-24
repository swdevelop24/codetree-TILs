a=input().split()
matha=int(a[0])
enga=int(a[1])
b=input().split()
mathb=int(b[0])
engb=int(b[1])

if matha > mathb:
    print('A')
elif matha < mathb:
    print('B')
elif matha==mathb:
    if enga>engb:
        print('A')
    else:
        print('B')