import copy
from collections import deque

N = int(input())    #미생물의 수 N
temp = input().split()  #미생물의 초기 크기
arr = deque([[] for _ in range(N)])   #미생물의 초기 위치 및 크기 담긴 배열
for i in range(N):
    arr[i] = [i + 1, int(temp[i])]

while len(arr) > 1: #미생물 1마리 남을 때까지 반복
    # for i in range(len(arr)):
    i = 0


    new_arr = []
    absorbed = []
    # copy_arr = copy.deepcopy(arr)
    # for i in range(arr):
    #     absorb = 0
    #     if i != 0 and arr[i][1] >= arr[i - 1][1]:   #왼쪽 미생물과 크기 비교후 흡수
    #         new = [i + 1, arr[i][1] + arr[i - 1][1]]
    #         absorb += 1
    #         copy_arr.deque
    #     if i != N - 1 and arr[i][1] >= arr[i + 1][1]:   #오른쪽 미생물과 크기 비교후 흡수
    #         if absorb == 0: #왼쪽 미생물 흡수안한 경우
    #             new = [i + 1, arr[i][1] + arr[i + 1][1]]
    #         else:   #왼쪽 미생물 흡수한 경우
    #             new = [new[0], new[1] + arr[i + 1][1]]
    #             absorb += 2
    # for i in range(arr):
    #     if i in absorbed:   #흡수된 미생물의 인덱스인 경우
    #         continue
    #     if i == 0 and arr[i][1] >= arr[i + 1][1]:   #가장 왼쪽 미생물인 경우
    #         new_arr.append([i + 1, arr[i][1] + arr[i + 1][1]])  #오른쪽 미생물과 크기 비교 후 흡수
    #         absorbed.append(i + 1)  #흡수했으면 new_arr, absorbed에 넣어주기
    #     elif i == n - 1 and arr[i][1] >= arr[i - 1][1]:   #가장 오른쪽 미생물인 경우
    #         new_arr.append([i + 1, arr[i][1] + arr[i - 1][1]])

