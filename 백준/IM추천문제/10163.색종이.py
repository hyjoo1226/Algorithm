N = int(input())    #색종이 개수 N
arr = [[0] * 1001 for _ in range(1001)] #1001x1001 배열
for i in range(N):
    xy_lst = list(map(int, input().split()))    #색종이 좌표, 너비, 높이
    for a in range(xy_lst[1], xy_lst[1] + xy_lst[3]): #좌표 0 시작이 위던 아래던 같은 결과
        for b in range(xy_lst[0], xy_lst[0] + xy_lst[2]):
            if arr[a][b] != i + 1:  #색종이 놓은 곳에 해당 넘버 기록(몇번째 색종이인지)
                arr[a][b] = i + 1

paper_dict = {} #각 색종이 면적 기록할 딕셔너리
for i in range(N):
    paper_dict[i + 1] = 0

for i in range(1001):   #각 색종이 면적 딕셔너리에 입력
    for j in range(1001):
        if arr[i][j] != 0:
            paper_dict[arr[i][j]] += 1

for v in paper_dict.values():
    print(v)