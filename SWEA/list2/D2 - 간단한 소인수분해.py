T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    num_lst = [2, 3, 5, 7, 11]  #소인수분해에 사용될 숫자 리스트
    count_lst = [0, 0, 0, 0, 0] #각 숫자 별 소인수분해 횟수를 담을 리스트
    for i in range(5):  #각 숫자로 나눴을 때 나머지가 없는 동안 N을 나누고, 해당 숫자의 카운트 1 증가
        while N % num_lst[i] == 0:
            N = N / num_lst[i]
            count_lst[i] += 1
    print(f'#{test_case}', end = ' ')
    for item in count_lst:
        print(item, end = ' ')
    print()