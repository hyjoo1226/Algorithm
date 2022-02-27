https://programmers.co.kr/learn/courses/30/lessons/42842

전체 카펫 개수의 약수를 구한 뒤 가장 차가 적은 곱셈쌍이 answer가 됨
```
def solution(brown, yellow):
    answer = []
    factor = []
    num = int(brown) + int(yellow)
    for i in range(1, num + 1):
        if num % i == 0:
            factor.append(i)
    factor_len = len(factor)
    if (factor_len % 2 == 0):
        answer.append(factor[int(factor_len / 2)])
        answer.append(factor[int(factor_len / 2) - 1])
    else:
        answer.append(factor[int((factor_len - 1) / 2)])
        answer.append(factor[int((factor_len - 1) / 2)])
    print(factor)
    return answer
```
4,6,7 테스트케이스 실패 => https://programmers.co.kr/questions/10292 https://programmers.co.kr/questions/15799 참고

수식으로 구하기(가로가 a, 세로가 b일때) =>

1. a >= b

2. brown = 2a + 2b - 4

3. yellow = (a - 2) * (b - 2) = ab - brown

```
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for b in range(1, total + 1):
        if (total / b) % 1 == 0:
            a = total / b
            if a >= b:
                if 2 * a + 2 * b == brown + 4:
                    return [a, b]
```