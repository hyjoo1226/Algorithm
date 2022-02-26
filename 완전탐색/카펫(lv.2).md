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
4,6,7 테스트케이스 실패 => https://programmers.co.kr/questions/10292 https://programmers.co.kr/questions/15799 참고 => 

```

```