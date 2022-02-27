https://programmers.co.kr/learn/courses/30/lessons/42840

반복되는 구간을 잘라 리스트를 만든다. 그 구간의 인덱스 수만큼 나누기하여 비교

```
def solution(answers):
    answer = []
    one = [1,2,3,4,5] 
    two = [2,1,2,3,2,4,2,5] 
    three = [3,3,1,1,2,2,4,4,5,5]
    count_one = 0
    count_two = 0
    count_three = 0
    for i in range(len(answers)): 
        if answers[i] == one[i % 5]: 
            count_one += 1 
        if answers[i] == two[i % 8]: 
            count_two += 1 
        if answers[i] == three[i % 10]: 
            count_three += 1 
    temp = [count_one, count_two, count_three] 
    for person, score in enumerate(temp): 
        if score == max(temp): 
            answer.append(person+1)    
    return answer
```