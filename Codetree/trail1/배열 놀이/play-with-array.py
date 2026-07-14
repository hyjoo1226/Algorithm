N, Q = map(int, input().split())
n_lst = list(map(int, input().split()))

for _ in range(Q):
    q_lst = list(map(int, input().split()))
    if q_lst[0] == 1:
        for i in range(1, len(q_lst)):
            print(n_lst[q_lst[i] - 1])

    elif q_lst[0] == 2:
        for i in range(1, len(q_lst)):
            try:
                pos = n_lst.index(q_lst[i])
                print(pos + 1)
            except:
                print(0)
    else:
        for i in range(1, len(q_lst), 2):
            for j in range(q_lst[i] - 1, q_lst[i + 1]):
                print(n_lst[j], end = ' ')
        print()