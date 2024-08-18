T = int(input())
for tc in range(1, T + 1):
    N = int(input())    #값
    price = [0] * 8

    count = 0
    while N >= 50000:
        N -= 50000
        count += 1
    price[0] = count

    count = 0
    while N >= 10000:
        N -= 10000
        count += 1
    price[1] = count

    count = 0
    while N >= 5000:
        N -= 5000
        count += 1
    price[2] = count

    count = 0
    while N >= 1000:
        N -= 1000
        count += 1
    price[3] = count

    count = 0
    while N >= 500:
        N -= 500
        count += 1
    price[4] = count

    count = 0
    while N >= 100:
        N -= 100
        count += 1
    price[5] = count

    count = 0
    while N >= 50:
        N -= 50
        count += 1
    price[6] = count

    count = 0
    while N >= 10:
        N -= 10
        count += 1
    price[7] = count

    print(f'#{tc}')
    print(*price)