N_lst = [0] * 9
for i in range(9):
    N_lst[i] = int(input())

temp = []
nan_sum = 0
token = 1
while token:
    for a in range(9):
        for b in range(a + 1, 9):
            for c in range(b + 1, 9):
                for d in range(c + 1, 9):
                    for e in range(d + 1, 9):
                        for f in range(e + 1, 9):
                            for g in range(f + 1, 9):
                                nan_sum = N_lst[a] + N_lst[b] + N_lst[c] + N_lst[d] + N_lst[e] + N_lst[f] + N_lst[g]
                                if nan_sum == 100:
                                    temp = [N_lst[a], N_lst[b], N_lst[c], N_lst[d], N_lst[e], N_lst[f], N_lst[g]]
                                    token = 0

temp.sort()
for item in temp:
    print(item)