n = int(input())

# Please write your code here.
def print_n(n):
    cnt = 0
    for _ in range(n):
        for _ in range(n):
            if cnt == 9:
                cnt = 0
            cnt += 1
            print(cnt, end=' ')
        print()

print_n(n)