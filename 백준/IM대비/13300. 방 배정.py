N, K = map(int, input().split())    #학생 수 N, 한 방 인원 K

girl = [0] * 6  #여학생 1~6학년
boy = [0] * 6   #남학생 1~6학년
for i in range(N):
    a, b = map(int, input().split())    #성별 a, 학년 b
    if a == 0:  #여학생
        girl[b - 1] += 1
    else:   #남학생
        boy[b - 1] += 1

room = 0    #방 개수
for i in range(6):  #1 ~ 6학년
    while girl[i] - K > 0:  #방 배정
        room += 1
        girl[i] -= K
    if 0 < girl[i] <= K:
        room += 1
    while boy[i] - K > 0:
        room += 1
        boy[i] -= K
    if 0 < boy[i] <= K:
        room += 1

print(room)