https://programmers.co.kr/learn/courses/30/lessons/42746

3, 30, 34가 있을 때 34, 3, 30 순으로 붙여짐. 3이 33이 되는 것.

3자리수이므로 3을 333으로 생각해야 함.

완전탐색을 할 경우 시간초과 문제 발생

원소가 0인 경우를 고려해 int 변환 후 str 변환

```
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
```