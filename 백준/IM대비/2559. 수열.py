N, K = map(int, input().split())    #전체 날짜 수 N, 연속적인 날짜 수 K
tem_lst = list(map(int, input().split()))   #온도 리스트
max_sum = -9999    #온도 최댓값
for i in range(N - K - 2):
    sum = 0
    for j in range(K):
        sum += tem_lst[i + j]
    print(sum)
    if max_sum < sum:
        max_sum = sum
print(max_sum)