def solution(arr):
    answer = 1
    final_dict = {}   #최종 딕셔너리
    for item in arr:
        a = item
        dict = {}   #약수 담을 딕셔너리
        while a != 1:    # 해당 수가 1이 될 때까지 반복
            for num in range(2, a + 1):  #작은 수부터 나눠서
                if a % num == 0: #나눠진다면
                    a = a // num   #나눈 값 대입
                    if dict.get(num) == None:   #딕셔너리에 없으면 추가, 있으면 1 증가
                        dict[num] = 1
                    else:
                        dict[num] += 1
                    break
                
        for k, v in dict.items(): #딕셔너리 병합, 기존에 있는 key인데 더 큰 value면 업데이트
            if final_dict.get(k) == None:
                final_dict[k] = v
            else:
                if final_dict[k] < v:
                    final_dict[k] = v
                    
    for k, v in final_dict.items():   #최소공배수 구하기
        for i in range(v):
            answer *= k
            
    return answer