a, b = map(int, input().split())

def prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def jjack(n):
    str_n = str(n)
    total = 0
    for i in range(len(str_n)):
        total += int(str_n[i])
    if total % 2 == 0:
        return True
    else:
        return False

cnt = 0
for i in range(a, b + 1):
    if prime_num(i) and jjack(i):
        cnt += 1

print(cnt)