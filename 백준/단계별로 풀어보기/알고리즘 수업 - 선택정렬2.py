#백준 23882 <알고리즘 수업 - 선택정렬 2>
#주어진 배열을 선택정렬(오름차순)할 때 K번 교환이 발생한 직후의 배열을 출력해라
#배열의 인덱스 끝부터 정렬(1회차에 가장 큰 값이 배열의 끝에 위치하도록)


def selection_sort(arr, K):
    for i in range(N - 1, 0, -1):   # (N - 1) ~ 1 범위
        min_idx = i
        for j in range(i - 1, -1, -1):  # (N - 2) ~ 0 범위
            if arr[min_idx] < arr[j]:   #min_idx 인덱스값을 가장 큰 정수가 있는 위치로 갱신
                min_idx = j
        if i == min_idx:    #갱신이 안되면 교환 발생 x(K 횟수에 포함되지 않음)
            pass
        else:   #갱신되면 교환 발생
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            K -= 1  #교환횟수 1 감소
            if K == 0:  #교환횟수가 0이되면 배열 리턴
                return arr
    return -1   #정렬이 끝났을때 교환횟수가 남아있다 -> K번 교환 전에 정렬이 완료됨. -1리턴


N, K = map(int, input().split())    #서로 다른 정수 N개, 교환 횟수 K
num_lst = list(map(int, input().split()))   #정수 리스트

result = selection_sort(num_lst, K) #선택정렬(오름차순)로 K번 교환했을 때의 배열 리턴
                                    #K번 교환 전에 정렬이 끝나면 -1 리턴
if result != -1:
    print(*result)
else:
    print(result)