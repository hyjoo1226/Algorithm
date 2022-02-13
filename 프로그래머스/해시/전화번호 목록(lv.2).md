https://programmers.co.kr/learn/courses/30/lessons/42577

배열을 각 항목의 길이순으로 정렬. 정렬을 통해 순회 횟수를 줄임

순회 돌면서 같은 경우 false return

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
1중 루프로 비교했지만 그래도 시간복잡도 문제 해결 못함

=> Hash 사용

1. Hash map을 만든다. (key: phone_number, value: 1 (숫자가 1개 존재))
2. temp(접두어)가 Hash map에 있다면 false
```
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

```