T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    #NxM 깃발
    flag = [0] * N
    for i in range(N):
        flag[i] = input()   #기존 깃발 입력

    count = 0  #색칠횟수
    for i in range(N):
        color_dict = {'W':0, 'B':0, 'R':0}  #각 색상 개수
        max_color = 0   #가장 많이 나온 색
        for j in range(M):
            if i == 0:
                if flag[0][j] != 'W':   #첫 줄 WHITE
                    count += 1
            elif i == N - 1:
                if flag[N - 1][j] != 'R':  #마지막 줄 RED
                    count += 1
            else:   #사이에 있는 줄
                color_dict[flag[i][j]] += 1 #해당 색상 밸류값 + 1
                
        for v in color_dict.values():   #가장 많이 나온 색
            if max_color < v:
                max_color = v
        count += M - max_color  #가장 많이 나온 색을 제외한 색들 색칠
        #####B가 없는 경우 고려해야함