N = int(input())
n_lst = list(map(int, input().split()))
n_lst.reverse()

for n in n_lst:
    if n % 2 == 0:
        print(n, end=' ')
