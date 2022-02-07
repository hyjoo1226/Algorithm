https://programmers.co.kr/learn/courses/30/lessons/42748

commands 이차원배열의 각 항목을 불러올때마다 정렬 후 answer 배열의 뒤에 추가

```
def solution(array, commands):
    answer = []
    for i, j, k in commands:    
        temp = array[i-1:j]
        print(temp)
        temp.sort()
        answer.append(temp[k-1])
    return answer
```
