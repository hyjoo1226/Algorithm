s = input()

for i in range(len(s)):
    if i == 1 or i == len(s) - 2:
        print('a', end='')
    else:
        print(s[i], end='')