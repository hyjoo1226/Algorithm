T = int(input())

for test_case in range(1, T + 1):
    N = int(input())    #카드 장수
    num_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}   #key가 0~9고 value는 0인 딕셔너리 초기화
    nums = input()  #여백없이 주어진 각 카드숫자 문자열로 저장

    for num in nums:    #순회하며 일치하는 숫자 카드의 value값을 1증가
        num_dict[int(num)] += 1

    max_key = 0 #가장 많이 나온 카드숫자와 값
    max_num = 0
    for k, v in num_dict.items():
        if max_num <= v:
            max_num = v
            if max_key < k:
                max_key = k
    
    print(f'#{test_case} {max_key} {max_num}')


