string=input() 
slen = len(string)

string = list(string)
currlen=slen 
while currlen >1:
    idx = int(input())
    if idx > currlen:
        string.pop(currlen-1)
    else:
        string.pop(idx)
    currlen = len(string)
    print(''.join(string))