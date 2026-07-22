n1, n2 = map(int, input().split())
n1_lst = list(map(int, input().split()))
n2_lst = list(map(int, input().split()))

def is_subsequence(n1_lst, n2_lst, n1, n2):
    if n2 > n1:
        return False
        
    for i in range(n1 - n2 + 1):
        if n1_lst[i : i + n2] == n2_lst:
            return True
            
    return False

if is_subsequence(n1_lst, n2_lst, n1, n2):
    print("Yes")
else:
    print("No")

# if n2 > n1:
#     print("No")

# elif n2 == n1:
#     if n1_lst[0] != n2_lst[0]:
#         print("No")
#     else:
#         print("Yes")

# else:
#     pre_idx = []
#     for i in range(n1):
#         if n1_lst[i] == n2_lst[0] and i + n2 + 1 <= n1:
#             pre_idx.append(i)

#     temp = []
#     for idx in pre_idx:
#         for i in range(n2):
#             if n2_lst[i] != n1_lst[idx + i]:
#                 temp.append(i)
#                 break

#     if len(pre_idx) == len(temp):
#         print("No")
#     else:
#         print("Yes")
        