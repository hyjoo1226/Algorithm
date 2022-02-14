https://programmers.co.kr/learn/courses/30/lessons/42578

# from itertools import combinations

def solution(clothes):
    answer = 0
    all_comb = 0
    for i in range(len(clothes)):
        all_comb = all_comb + i + 1

    kind = []
    for i in clothes:
        kind.append(i[1])
    kind.sort()
    print(kind)

    # hash_map = {}
    # for i in clothes:
    #     hash_map[i[0]] = i[1]
    # value_len = 0
    # for value in hash_map:
    #     value_len += 1
    # print(value_len)
    
    # sorted_hash = sorted(hash_map, key = lambda x : hash_map[x])
    # print(sorted_hash)
    
# 전체 조합(순서x 중복x) - value값 겹치는 조합들
    return answer