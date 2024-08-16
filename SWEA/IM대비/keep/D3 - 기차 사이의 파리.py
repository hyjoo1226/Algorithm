T = int(input())
for tc in range(1, T + 1):
    D, A, B, F = map(int, input().split())  #D 거리, A,B 속력, F 파리속력

    # 0AF ~ 250B
    T = D / (A + B) #A와B가 닿을때까지 걸린 시간 T
    FT = D / (F + B)    #파리와 B가 닿을떄까지 걸린 시간
    count = B = F * FT
    A = A * FT