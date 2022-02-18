https://programmers.co.kr/learn/courses/30/lessons/42578

의상의 종류에 따른 모든 조합을 만들었을 때

조합의 각 항목이 1개씩 있는 경우를 따로 뽑아 all_comb에 넣어서 길이 return

```
from itertools import combinations
from collections import Counter

def solution(clothes):
    answer = 0
    kind = []
    all_comb = []
    for i in clothes:
        kind.append(i[1])
    kind.sort()
    for i in range(len(kind)):
        temp = list(combinations(kind, i + 1))
        for j in temp:
            temp2 = Counter(j).most_common()
            if temp2[0][1] == 1:
                all_comb.append(j)
    answer = len(all_comb)
    return answer
```

=> 일부 항목 시간복합도 문제 발생

서로 다른 옷의 조합의 수 = (각 종류별 옷의 개수 + 1)을 전부 곱한 값에 - 1(아무것도 입지 않은 경우)

모든 주합을 구하지 않더라도 각 옷의 개수만 알면 됨
```
def solution(clothes):
    kind = []
    for i in clothes:
        kind.append(i[1])
    kind.sort()
    temp = kind[0]
    count = 0
    result = 1

    for name in kind:
        if name == temp:
            count = count + 1
        else:
            result = result * (count + 1)
            count = 1
            temp = name
            print("temp:", temp)
    result = result * (count + 1)
    return result - 1
```