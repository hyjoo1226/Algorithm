N = int(input())    #기둥의 개수
pos_lst = []    #각 기둥의 왼쪽 면 위치
height_lst = [] #각 기둥의 높이
for i in range(N):
    L, H = map(int, input().split())
    pos_lst.append(L)
    height_lst.append(H)

for i in range(len(pos_lst) - 1):    #오름차순 선택정렬
    min_idx = i
    for j in range(i + 1, len(pos_lst)):
        if pos_lst[min_idx] > pos_lst[j]:
            min_idx = j
    pos_lst[i], pos_lst[min_idx] = pos_lst[min_idx], pos_lst[i]
    height_lst[i], height_lst[min_idx] = height_lst[min_idx], height_lst[i]

area = 0    #전체넓이
max_height = height_lst[0]  #가장 높은 높이
check_idx = 0   #가장 높은 높이 인덱스
temp = max(height_lst)
for i in range(1, N):
    if max_height != temp:   #가장 높은 높이 도달때까지 넓이 합
        if height_lst[i] > height_lst[i - 1]:
            area += (pos_lst[i] - pos_lst[i - 1]) * max_height
            max_height = height_lst[i]
        else:
            area += (pos_lst[i] - pos_lst[i - 1]) * max_height
    else:   #가장 높은 높이 도달했으면 위치 기록 후 종료
        check_idx = i
        area += temp
        break

max_height = height_lst[-1]
for i in range(N - 1, check_idx - 1, -1):
    if max_height != temp:
        if height_lst[i] < height_lst[i - 1]:
            area += (pos_lst[i] - pos_lst[i - 1]) * max_height
            max_height = height_lst[i]
        else:
            area += (pos_lst[i] - pos_lst[i - 1]) * max_height

print(area)
#반례 최고높이건물 붙어있는경우
# 5
# 1 5
# 2 1
# 3 1
# 4 1
# 5 5