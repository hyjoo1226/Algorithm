https://programmers.co.kr/learn/courses/30/lessons/43165

dfs 재귀함수

각 numbers는 +인 경우, -인 경우가 있다. 이 경우들을 고려해 계속 가지치기하며 result값을 합산해나감

가지치기가 끝났을 때 result값과 타겟넘버 비교
```
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0,0)
    return answer
```