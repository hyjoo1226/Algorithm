a_l, b_l = map(int, input().split())
a_n = list(map(int, input().split()))
b_n = list(map(int, input().split()))

a_index = []
t_flag = 0

for i in range(a_l):
    if a_n[i] == b_n[0]:
        a_index.append(i)

for a_i in a_index:
    flag = 0

    if a_i + b_l > a_l:
        continue

    for j in range(b_l):
        if a_n[a_i + j] != b_n[j]:
            flag = 1
            break
    if flag == 0:
        print("Yes")
        t_flag = 1
        break
        
if t_flag == 0:        
    print("No")
