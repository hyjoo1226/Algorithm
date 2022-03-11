https://programmers.co.kr/learn/courses/30/lessons/42862
탐욕법: 미래를 생각하지 않고 현재 최선의 선택지를 고르는 알고리즘

lost가 3,5 reserve가 4,6일 때 reserve4가 lost5를 빌려주는 경우보다 reserve4가 lost3, reserve6이 lost5를 빌려주는 경우가 더 최선이다. 따라서 reserve가 lost의 왼쪽부터 빌려나가도록 구현


```
def solution(n, lost, reserve):
    #lost, reverse 중복된 케이스 제거
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i - 1)
        elif i + 1 in set_lost:
            set_lost.remove(i + 1)
    return n - len(set_lost)
```