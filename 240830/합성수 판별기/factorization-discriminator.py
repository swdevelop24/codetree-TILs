n=int(input())
composite=False
for i in range(2, n):
    if n%i==0:
        composite=True
        break
if composite:
    print("C")
else:
    print("N")