A =input()

def palindrome(A):
    n=len(A)
    for x in range(n):
        if A[x] != A[n-1-x]:
            return False
    return True

if palindrome(A):
    print("Yes")
else:
    print("No")