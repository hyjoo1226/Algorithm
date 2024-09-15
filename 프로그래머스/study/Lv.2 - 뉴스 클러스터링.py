def check_str(str):  #알파벳인지 검사 후 원소 딕셔너리 반환
    char_dict = {}
    temp = ''
    for char in str:
        if char.isupper() == True:  #알파벳 대문자면 소문자로 변환해서 추가
            temp += char.lower()
        elif char.islower() == True:  #알파벳 소문자면 추가
            temp += char
        else:  #알파벳아니면 넘어가기
            temp = ''
            continue

        if len(temp) == 2:  #길이가 2가 되면
            if char_dict.get(temp) == None:  #원소 딕셔너리에 없다면 추가
                char_dict[temp] = 1
            else:  #이미 있다면 값 +1
                char_dict[temp] += 1
            temp = temp[1]  #앞 문자 버리기

    return char_dict


def solution(str1, str2):
    answer = 0

    str1_dict = check_str(str1) #알파벳인지 검사 후 원소 딕셔너리 반환
    str2_dict = check_str(str2)

    if str1_dict == {} and str2_dict == {}:  #두 집합이 모두 공집한인 경우
        return 65536

    num_inter = 0   #교집합 원소 개수
    num_union = 0   #합집합 원소 개수
    for k, v in str1_dict.items():  #str2_dict에 병합
        if str2_dict.get(k) == None:    #key가 없다면 추가
            str2_dict[k] = v
        else:
            num_inter += min(str1_dict[k], str2_dict[k])  #key가 이미 있다면 작은 value로 교집합 원소 개수 더해주기
            if str1_dict[k] > str2_dict[k]: #value가 더 크다면 갱신
                str2_dict[k] = v

    for v in str2_dict.values():    #합집합 원소 개수 구하기
        num_union += v

    answer = int((num_inter / num_union) * 65536)  #자카드 유사도 구하기

    return answer