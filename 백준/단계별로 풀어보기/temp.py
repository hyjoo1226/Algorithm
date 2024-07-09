A, B = input().split()
A_r = ''
B_r = ''
for i in A:
    A_r = i + A_r
for i in B:
    B_r = i + B_r
if int(A_r) > int(B_r):
    print(A_r)
else:
    print(B_r)