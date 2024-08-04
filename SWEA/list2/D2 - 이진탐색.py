def binary_search(P, key):  #이진검색 0부터 1씩 증가하는 값이므로 따로 배열X
    start = 1
    end = P
    search_count = 0
    while start <= end:
        middle = (start + end) // 2
        search_count += 1

        if middle == key:
            return search_count
        elif middle > key:
            end = middle   #문제에서 중간페이지를 포함해서 다시 서치하라고 나와있음
        else:
            start = middle

T = int(input())

for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split()) #전체쪽수 P, a와 b가 찾아야 할 쪽수 Pa,Pb

    A_count = binary_search(P, Pa)
    B_count = binary_search(P, Pb)

    if A_count < B_count:   #A가 이기면 A, B가 이기면 B, 비기면 0
        result = 'A'
    elif A_count > B_count:
        result = 'B'
    else:
        result = 0

    print(f'#{tc} {result}')