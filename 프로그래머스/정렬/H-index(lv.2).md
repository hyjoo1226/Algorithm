https://programmers.co.kr/learn/courses/30/lessons/42747#

배열 오름차순 정렬 후 

i번째 논문이 인용된 횟수가

위의 조건을 충족하는 논문의 개수보다 크거나 같아지는 값

```
def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            return len(citations) - i
    return 0
```