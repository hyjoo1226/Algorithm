target = input()
s_lst = ["apple", "banana", "grape", "blueberry", "orange"]
n_target = 0

for s in s_lst:
    if target in [s[2], s[3]]:
        print(s)
        n_target += 1

print(n_target)