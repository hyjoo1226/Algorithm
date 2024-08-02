T = int(input())

for test_case in range(1, T + 1):
    K, N, M = input().split()
    charge_station = list(map(int, input().split()))    #충전기가 설치된 정류장
    K = int(K)  #한번 충전으로 최대한 이동할 수 있는 정류장의 수
    N = int(N)  #정류장의 수 (N은 종점)
    M = int(M)  #충전기가 설치된 정류장의 개수