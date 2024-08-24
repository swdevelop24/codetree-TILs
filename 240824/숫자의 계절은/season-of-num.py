m=int(input())
if m>=9 and m<=11:
    print("Fall")
elif m>=6:
    print("Summer")
elif m>=3:
    print("Spring")
elif m>=2 or m==12:
    print("Winter")