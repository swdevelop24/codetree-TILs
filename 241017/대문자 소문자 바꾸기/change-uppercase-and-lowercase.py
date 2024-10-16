arr = input()

for ch in arr:
    if ch >='a' and ch <='z':
        print(ch.upper(), end='')
    else:
        print(ch.lower(), end='')