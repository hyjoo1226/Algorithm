from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for perm in permutations(dungeons, len(dungeons)):
        stamina = k
        count = 0
        for need, cost in perm:
            if need <= stamina:
                stamina -= cost
                count += 1
            else:
                break
        
        answer = max(answer, count)
    
    return answer