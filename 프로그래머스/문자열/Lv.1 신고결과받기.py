def solution(id_list, report, k):
    answer = [0] * len(id_list)
    user = {}
    report = list(set(report))
    
    for item in id_list:
        user[item] = 0
    
    for item in report:
        index = item.find(" ")
        temp = item[index + 1:]
        user[temp] += 1
    
    report_list = []
    for key, value in user.items():
        if value >= k:
            report_list.append(key)
    
    mail_list = []
    for item in report:
        index = item.find(" ")
        temp1 = item[:index]
        temp2 = item[index+1:]
        
        if temp2 in report_list:
            answer[id_list.index(temp1)] += 1     
    
    return answer