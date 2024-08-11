from pprint import pprint

width, length = map(int, input().split())   #가로 세로
cut = int(input())  #자르는 횟수
width_lst = [0, length]
length_lst = [0, width]
for k in range(cut):
    direction, number = map(int, input().split())   #방향(0이면 가로, 1이면 세로), 자르는 점선 번호
    if direction == 0:
        width_lst.append(number)
    else:
        length_lst.append(number)
width_lst.sort()    #자르는 위치 오름차순 정렬
length_lst.sort()
max_area = 0
for i in range(1, len(width_lst)):
    for j in range(1, len(length_lst)):
        A = width_lst[i] - width_lst[i - 1]
        B = length_lst[j] - length_lst[j - 1]
        temp = A * B    #넓이
        if max_area < temp:
            max_area = temp
print(max_area)


#     if direction == 0:
#         count += 1
#         for i in range(length):
#             for j in range(width):
#
#                 if i < number:  #각 구역 매핑
#                     if use_dict.get(arr[i][j]) == None:
#                         count += 1
#                         use_dict[arr[i][j]] = 0
#                     arr[i][j] = count
#                     # if arr[i][j] == temp:
#                     #     arr[i][j] = count_one
#                     # else:
#                     #     arr[i][j] = count_two
#
#     else:
#         temp = arr[0][0]
#         count_one += 1
#         count_two -= 1
#         for i in range(length):
#             for j in range(width):
#                 if j < number:
#                     if arr[i][j] == temp:
#                         arr[i][j] = count_one
#                     else:
#                         arr[i][j] = count_two
#
#     pprint(arr)
# k_dict = {}
# for i in range(length):
#     for j in range(width):
#         if k_dict.get(arr[i][j]) == None:   #딕셔너리에 없는 값이면 1을 값으로 가지고 키 추가
#              k_dict.setdefault(arr[i][j], 1)
#         else:
#             k_dict[arr[i][j]] += 1
# print(k_dict)
# max_sum = 0 #가장 큰 밸류값이 가장 큰 넓이
# for v in k_dict.values():
#     if max_sum < v:
#         max_sum = v
# print(max_sum)
