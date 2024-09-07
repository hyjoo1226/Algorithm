T = int(input())
for tc in range(1, T + 1):
    N = int(input())    #신청서 개수 N
    arr = [list(map(int, input().split())) for _ in range(N)]   #각 리스트 첫 항 시작시간, 두번째 항 종료시간
    s_arr = sorted(arr) #시작시간 기준으로 정렬

    cnt = 0 #작업 횟수
    #순열로 모든 경우 구하고, 작업 시작시간이 끝나는시간보다 늦으면 제외
