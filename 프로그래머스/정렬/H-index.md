https://programmers.co.kr/learn/courses/30/lessons/42747#

```
def solution(citations):
    answer = 0
    h = 0
    for i in citations:
        h = i;
        count = 0
        for j in citations:
            if j >= h:
                count = count + 1
        if h == count:
            answer = count
        h가 count와 같은 경우가 없다면 count보다 작은 최대값
    print(answer)
    return answer
```