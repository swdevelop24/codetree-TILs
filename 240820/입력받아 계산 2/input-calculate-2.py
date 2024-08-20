# python에서 입력은 한 줄 단위로만 받을 수 있음
# 2개의 숫자를 한 줄에 공백을 사이에 두고 받고 싶다면
# 문자열을 특정기준으로 잘라주는 함수 split() 
c=input().split()
print(int(c[0])*int(c[1]))