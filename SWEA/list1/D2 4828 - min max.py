T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    a_lst = list(map(int, input().split()))
    num_min = a_lst[0]
    num_max = a_lst[0]
    
    for item in a_lst:
        if num_min > item:
            num_min = item
        if num_max < item:
            num_max = item
            
    print(f'#{test_case} {num_max - num_min}')