A, B = map(int, input().split())

print(A, end=' ')
print(B, end=' ')
for i in range(8):
    if i % 2 == 0:
        A = (A + B) % 10
        print(A, end=' ')
    else:
        B = (A + B) % 10
        print(B, end=' ')
