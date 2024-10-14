A = input()

encoding=""
prev_char=A[0]
total=1

for curr_char in A[1:]:
    if curr_char == prev_char:
        total+=1
    else:
        encoding+=prev_char
        encoding+=str(total)

        prev_char = curr_char
        total =1 
    
encoding+=prev_char
encoding+=str(total) 

print(len(encoding))
print(encoding)