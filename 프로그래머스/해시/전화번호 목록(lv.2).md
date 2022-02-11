https://programmers.co.kr/learn/courses/30/lessons/42577

배열을 각 항목의 길이순으로 정렬

두번 순회 돌면서 같은 경우 false return

```
def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    i = 0
    while (i < len(phone_book)):
        j = i + 1
        while (j < len(phone_book)):
            if (phone_book[j].find(phone_book[i]) > -1):
                answer = False
                return answer
            j += 1
        i += 1
    return answer
```
=> 시간복잡도 문제 해결 못함