



# def selection_sort(arr, length): #선택정렬
#     global change
#     for i in range(length - 1):
#         max_idx = i #가장 큰 값
#         min_idx = i #가장 작은 값
#         for j in range(i + 1, length):
#             if arr[max_idx] <= arr[j]:  #가장 큰 값 중 뒤에 있는 값
#                 max_idx = j
#             if arr[min_idx] > arr[j]:   #가장 작은 값 중 앞에 있는 값
#                 min_idx = j
#         if i == max_idx: #갱신이 안되면 교환 발생x(change 값 그대로)
#             pass
#         else:   #갱신되면 교환 발생
#             arr[min_idx], arr[max_idx] = arr[max_idx], arr[min_idx]
#             change -= 1 #교환횟수 1 감소
#             if change == 0: #교환횟수가 0이되면 배열 리턴
#                 return arr
#     return arr
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     temp, change = input().split()
#     change = int(change)
#     length = len(temp)  #숫자판 길이
#     N_lst = [0] * length
#     for i in range(length):
#         N_lst[i] = temp[i]  #주어진 숫자판 N(문자열 형태로), 교환횟수 change
#
#     N_lst = selection_sort(N_lst, length)   #선택정렬
#     while change > 0:   #교환횟수 남아있으면 뒤에 두개 반복해서 교환
#         N_lst[-1], N_lst[-2] = N_lst[-2], N_lst[-1]
#         change -= 1
#
#     print(f'#{tc}', end = ' ')
#     for item in N_lst:
#         print(item, end = '')
#     print()

