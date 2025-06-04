def solution(n, arr1, arr2):
    answer = []
    bin_arr1 = []
    bin_arr2 = []
    for item in arr1:
        bin_arr1.append(bin(item))
    for item in arr2:
        bin_arr2.append(bin(item))
        
    for i in range(n):
        temp1 = list(bin_arr1[i])
        temp2 = list(bin_arr2[i])
        temp1 = temp1[2:]
        temp2 = temp2[2:]
        
        if len(temp1) < n:
            while len(temp1) != n:
                temp1.insert(0, '0')
        elif len(temp1) > n:
            while len(temp1) != n:
                temp1.pop()
            
        if len(temp2) < n:
            while len(temp2) != n:
                temp2.insert(0, '0')
        elif len(temp2) > n:
            while len(temp2) != n:
                temp2.pop()
            
        bin_arr1[i] = temp1
        bin_arr2[i] = temp2
    
    new_arr = [['0'] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if bin_arr1[i][j] == '1' or bin_arr2[i][j] == '1':
                new_arr[i][j] = '#'
            else:
                new_arr[i][j] = ' ' 
    for i in range(n):
        answer.append(''.join(new_arr[i]))

    return answer