input_str = input()
target_str = input()

# Please write your code here.
lst = []
for i in range(len(input_str)):
    if target_str[0] == input_str[i]:
        lst.append(i)
flag_2 = 0

for l in lst:
    flag = 0
    for j in range(len(target_str)):
        if l + j >= len(input_str):
            flag = 1
            continue
        if target_str[j] != input_str[l + j]:
            flag = 1
    if flag == 0:
        print(l)
        flag_2 = 1
        break

if flag_2 != 1:
    print(-1)