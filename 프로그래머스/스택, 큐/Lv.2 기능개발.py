from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque(progresses)
    queue_s = deque(speeds)
    while queue:
        for i in range(len(queue)):
            queue[i] += queue_s[i]
        
        count = 0
        for q in queue:
            if q < 100:
                break
            else:
                count += 1

        if count:
            for i in range(count):
                queue.popleft()
                queue_s.popleft()
            answer.append(count)
                
    return answer