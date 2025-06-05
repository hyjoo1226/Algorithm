from itertools import combinations

def solution(orders, course):
    answer = []
    for c in course:
        c_dict = {}
        for order in orders:
            for p in combinations(sorted(order), c):
                temp = ''.join(p)
                if not temp in c_dict:
                    c_dict[temp] = 1
                else:
                    c_dict[temp] += 1
                    
        if not c_dict:
            continue
            
        sort_dict = sorted(c_dict.items(), key=lambda x: x[1], reverse=True)

        max_value = sort_dict[0][1]
        if max_value < 2:
            continue
        else:
            for key, value in sort_dict:
                if value == max_value:
                    answer.append(key)
                else:
                    break
    answer.sort()
            
    return answer