def solution(files):
    answer = []
    part_files = []
    
    for item in files:
        head = ''
        num = ''
        tail = ''
        for cha in item:
            if len(num) == 0 and not cha.isdigit():
                head += cha
            elif len(tail) == 0 and len(num) < 5 and cha.isdigit():
                num += cha
            else:
                tail += cha
        part_files.append([head, num, tail])
    
    sort_files = sorted(part_files, key=lambda x: (x[0].lower(), int(x[1])))
    
    for item in sort_files:
        answer.append(''.join(item))
    
    return answer