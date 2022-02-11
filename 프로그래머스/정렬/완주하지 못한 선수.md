https://programmers.co.kr/learn/courses/30/lessons/42576

두 배열 모두 순회 => 시간복잡도 문제 발생

두 배열 정렬 후 completion 배열을 순회하면서 다른 이름이 담기는 경우 return

순회가 끝났다면 마지막 인덱스 return

```
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    i = 0
    while (i < len(completion)):
        if (participant[i] != completion[i]):
            return participant[i]
        i = i + 1
    return participant[i]
```