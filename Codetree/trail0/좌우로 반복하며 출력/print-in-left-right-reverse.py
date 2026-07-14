N = int(input())

row_data = []
for i in range(1, N + 1):
    row_data.append(i)

reverse_data = row_data[::-1]

for i in range(N):
    if i % 2 == 0:
        print("".join(map(str, row_data)))
    else:
        print("".join(map(str, reverse_data)))