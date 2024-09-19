def solution(n, times):
    answer = 0
    length = len(times)  #심사관 수
    times.sort()    #심사시간 오름차순 정렬

    if n <= length: #사람이 심사관 수보다 작거나 같으면
        return times[n - 1]

    #초기세팅
    n -= length #시작하자마자 심사받으러 감
    use = times[:]  #각 심사대 남은 시간
    t = 0   #걸린 시간
    rest = []   #빈 심사대
    while n:    #모든 사람이 심사를 받을 때까지
        t += 1  #시간 +1
        for i in range(length): #모든 심사대 순회
            use[i] -= 1 #심사대 남은 시간 -1
            if use[i] == 0: #심사 끝난 경우
                rest.append(i)  #빈 심사대에 추가

        for k in range(len(rest)):
            for i in range(length):
                if times[rest[k]] < use[i] + times[i]:  #빈 심사대의 총 시간이 다른 심사대의 남은 시간 + 총 시간보다 작다면
                    n -= 1  # 다음 사람 심사
                    use[rest[k]] = times[rest[k]]  # 심사 시간 초기화
                    rest.pop(k)  #빈 심사대에서 제외
                    break
                if rest[k] > i:  # 가지치기
                    break
    t += max(use)   #가장 오래 남은 심사대 시간 더해주기
    answer = t
    return answer

n = 6
times = [7, 10]
print(solution(n, times))