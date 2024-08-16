T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    N_lst = input().split('0')
    max_len = 0
    for item in N_lst:
        if item != '':
            if max_len < len(item):
                max_len = len(item)
    print(f'#{tc} {max_len}')


# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     N_str = input()
#
#     max_count = 0
#     count = 0
#     for char in N_str:
#         if char == '1':
#             count += 1
#         else:
#             if max_count < count:
#                 max_count = count
#             count = 0
#         if max_count < count:
#             max_count = count
#
#     print(f'#{tc} {max_count}')

# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = int(input())    #수열의 길이
#     numbers = input()   #0과 1로 구성된 수열
#
#     count = 0   #연속한 1의 개수
#     count_lst = []  #카운트들을 담을 리스트
#     for i in range(len(numbers)):
#         if numbers[i] == '1':   #x for x in count_lst] + [count]
#             count += 1
#             if i == len(numbers) - 1:
#                 count_lst = [x for x in count_lst] + [count]
#         else:
#             count_lst = [x for x in count_lst] + [count]
#             count = 0   #0을 만나면 count 리스트에 넣고, 0으로 초기화
#
#         max_count = 0
#         for item in count_lst:
#             if max_count < item:
#                 max_count = item
#
#     print(f'#{test_case} {max_count}')