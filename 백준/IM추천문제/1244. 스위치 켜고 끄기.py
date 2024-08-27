num_switch = int(input())   #스위치개수
switch = list(map(int, input().split()))    #스위치 상태 리스트로
students = int(input()) #학생수
for i in range(students):
    gender, select = map(int, input().split())  #성별(남 1 여 2), 받은 스위치
    if gender == 1: #남학생인 경우
        for k in range(1, num_switch + 1):
            if k % select == 0: #해당 스위치가 받은 스위치번호의 배수라면 상태를 바꾼다
                if switch[k - 1] == 0:
                    switch[k - 1] = 1
                else:
                    switch[k - 1] = 0

    else:   #여학생인 경우
        count = 0
        for k in range(1, num_switch + 1):
            if 1 <= select - k and select + k < num_switch + 1: #받은 스위치 번호 앞뒤로 같은 값이면 count + 1
                if switch[select - k - 1] == switch[select + k - 1]:
                    count += 1
                else:   #아니면 반복문 종료
                    break
        for j in range(select - count, select + count + 1): #받은 스위치 앞뒤로 카운트만큼 상태를 바꾼다
            if switch[j - 1] == 0:
                switch[j - 1] = 1
            else:
                switch[j - 1] = 0

for i in range(1, num_switch + 1):
    print(switch[i - 1], end = ' ')
    if i % 20 == 0:
        print()
