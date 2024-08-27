N, K = map(int, input().split())    #전체 날짜 수 N, 연속적인 날짜 수 K
tem_lst = list(map(int, input().split()))   #온도 리스트
max_sum = -9999    #온도 최댓값

arr = [tem_lst[0]] * N  #누적합 저장할 배열
for i in range(1, N):
    arr[i] = arr[i - 1] + tem_lst[i]

max_sum = arr[K - 1]
for i in range(0, N - K):
    if max_sum < arr[K + i] - arr[i]:
        max_sum = arr[K + i] - arr[i]

print(max_sum)


#시간초과(시간복잡도: O^2)
# for i in range(N - K + 1):
#     sum = 0
#     for j in range(K):
#         sum += tem_lst[i + j]
#     if max_sum < sum:
#         max_sum = sum
# print(max_sum)