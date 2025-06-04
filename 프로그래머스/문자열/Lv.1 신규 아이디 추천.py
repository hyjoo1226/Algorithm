def solution(new_id):
    answer = ''
    num_list = '0123456789'
    apt_list = 'abcdefghijklmnopqrstuvwxyz'
    id_str = new_id.lower()
    id_list = []
    for str in id_str:
        if str in num_list or str in apt_list or str == '-' or str == '_' or str == '.':
            if str == '.' and len(id_list) != 0 and id_list[-1] == '.':
                pass
            else:
                id_list.append(str)
    if len(id_list) != 0 and id_list[0] == '.':
        id_list.pop(0)
    if len(id_list) != 0 and id_list[-1] == '.':
        id_list.pop(-1)
    if len(id_list) == 0:
        id_list.append('a')
    if len(id_list) >= 16:
        id_list = id_list[0 : 15]
    if len(id_list) != 0 and id_list[-1]== '.':
        id_list.pop(-1)
    if len(id_list) <= 2:
        add_num = 3 - len(id_list)
        last_str = id_list[-1]
        for i in range(add_num):
            id_list.append(last_str)     
    answer = ''.join(id_list)
    print(answer)
    return answer