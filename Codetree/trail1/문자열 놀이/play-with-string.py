S, Q = input().split()

Q = int(Q)
S = list(S)

for _ in range(Q):
    qu = input().split()
    if qu[0] == '1':
        S[int(qu[1]) - 1], S[int(qu[2]) - 1] = S[int(qu[2]) - 1], S[int(qu[1]) - 1]
        for s in S:
            print(s, end='')
    
    if qu[0] == '2':
        for i in range(len(S)):
            if S[i] == qu[1]:
                S[i] = qu[2]
            print(S[i], end='')
    print()
