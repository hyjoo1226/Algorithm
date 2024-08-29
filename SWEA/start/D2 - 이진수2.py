T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    idx = 0 #해당 자리 인덱스
    result = ''
    while N != 0:
        idx += 1
        if idx == 13:
            result = 'overflow'
            break
        if N >= (0.5 ** idx): #해당 자리 있으면
            result += '1'
            N -= (0.5 ** idx)
        elif N != 0:
            result += '0'

    print(f'#{tc} {result}')