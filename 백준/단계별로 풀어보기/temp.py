S = input()
alpha = list(range(26))
temp = 'a'
count = 0

for i in alpha:
    alpha[i] = -1
for str in S:
    if alpha[ord(str) - ord(temp)] != -1:
        pass
    else:
        alpha[ord(str) - ord(temp)] = count
    count += 1
for i in alpha:
    print(i, end = " ")