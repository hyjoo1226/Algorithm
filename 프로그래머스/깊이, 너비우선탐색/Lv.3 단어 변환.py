from collections import deque

def solution(begin, target, words):
    answer = 0
    
    def diff(first, second):
        count = 0
        for i in range(len(first)):
            if first[i] != second[i]:
                count += 1
        if count == 1:
            return True
        else:
            return False
    
    used = [0] * len(words)
    queue = deque()
    queue.append([begin, 0])
    checker = 0
    
    while queue:
        current, depth = queue.popleft()
        if current == target:
            checker = 1
            return depth
        for i in range(len(words)):
            if used[i] == 0 and diff(current, words[i]):
                queue.append([words[i], depth + 1])
                used[i] = 1
    
    if checker == 1:
        answer = depth
        
    return answer