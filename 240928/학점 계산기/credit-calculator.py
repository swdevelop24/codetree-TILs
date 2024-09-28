n=int(input())

scores=list(map(float, input().split()))

avg = sum(scores)/n

if avg >=4.0: 
    print(f"{avg:.1f}")
    print("Perfect")
elif avg >3.0:
    print(f"{avg:.1f}")
    print("Good")
else:
    print(f"{avg:.1f}")
    print("Poor")