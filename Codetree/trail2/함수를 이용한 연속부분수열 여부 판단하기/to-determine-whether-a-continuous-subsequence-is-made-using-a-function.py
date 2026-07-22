n1, n2 = map(int, input().split())
n1_lst = list(map(int, input().split()))
n2_lst = list(map(int, input().split()))

if n2 > n1:
    print("No")

elif n2 == n1:
    if n1_lst[0] != n2_lst[0]:
        print("No")
    else:
        print("Yes")

else:
    pre_idx = []
    for i in range(n1):
        if n1_lst[i] == n2_lst[0] and i + n2 + 1 <= n1:
            pre_idx.append(i)

    temp = []
    for idx in pre_idx:
        for i in range(n2):
            if n2_lst[i] != n1_lst[idx + i]:
                temp.append(i)
                break

    if len(pre_idx) == len(temp):
        print("No")
    else:
        print("Yes")
        