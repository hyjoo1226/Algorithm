A = input()
B = input()

while A.find(B) != -1:
    A = A.replace(B, "")

print(A)

