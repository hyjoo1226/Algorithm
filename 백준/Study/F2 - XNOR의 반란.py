from collections import deque

def xnor(num1, num2, B):    #두 수 XNOR연산 결과 반환
    temp = ''
    for i in range(B):
        if num1[i] == num2[i]:
            temp += '1'
        else:
            temp += '0'
    return temp


def adjacent_subsets_iterative(arr):
    result = []
    n = len(arr)

    # 비트마스크를 사용하여 모든 가능한 조합 생성
    for mask in range(1 << n):
        subset = []
        valid = True
        last_selected = -2

        # 각 비트 확인
        for i in range(n):
            if mask & (1 << i):
                # 인접하지 않은 원소가 선택되었는지 확인
                if i - last_selected == 1:
                    subset.append(arr[i])
                elif not subset:  # 첫 원소 선택
                    subset.append(arr[i])
                else:
                    valid = False
                    break
                last_selected = i

        if valid and subset:
            result.append(subset)

    return result


N, B = map(int, input().split())    #N: 수의 개수, B: 사용하는 비트의 수
A = list(map(int, input().split())) #수 리스트
A_cvt = []  #A 변환

num_max = '1' * B    #B비트 정수 최댓값

for num in A:
    temp = str(bin(num)[2:]) # 문자열 2진수 변환
    while len(temp) < B:   #길이 맞춰주기
        temp = '0' + temp
    A_cvt.append(temp)

result = -1
C = adjacent_subsets_iterative(A_cvt)
for item in C:
    temp = deque(item[:])
    while len(temp) > 1:    #최후의 수가 남을 때까지 연산
        first = temp.popleft()  #복사해둔 temp에서 앞의 수 2개 빼고, 연산한 값 앞에 넣어주기
        second = temp.popleft()
        temp.appendleft(xnor(first, second, B))

    if temp[0] == num_max:  #해당 값이 최댓값과 같다면
        result = int(num_max, 2)
        break

    z_temp = deque(list(temp[0]))
    for char in temp[0]:  #앞에 0 값이 있다면 제거해주기
        if char == '0':
            z_temp.popleft()
        else:
            if result < int(''.join(z_temp), 2):
                result = int(''.join(z_temp), 2)
            break

print(result)