score1 =input().split()
score2 = input().split()
math1 = int(score1[0])
eng1=int(score1[1])
math2=int(score2[0])
eng2=int(score2[1])
if math1 >math2 and eng1 > eng2:
    print(1)
else:
    print(0)