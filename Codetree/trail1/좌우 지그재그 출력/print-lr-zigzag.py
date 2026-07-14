N = int(input())

cnt = 1

for i in range(N):
    row = []
    for _ in range(N):
        row.append(str(cnt))
        cnt += 1
    
    if i % 2 == 0:
        print(' '.join(row))
    else:
        print(' '.join(row[::-1]))