def solution(numbers):
    answer = []
    for i in range(1, len(numbers)):
        for j in range(0, i):
            a = numbers[i] + numbers[j]
            if a not in answer:
                answer.append(a)
    answer.sort()
        
    return answer