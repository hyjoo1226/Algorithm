T = int(input())
for tc in range(1, T + 1):
    N, hex = input().split()    #자리 수 N, 16진수 hex
    hex_dict = {'A' : 10, 'B' : 11, 'C' : 12, 'D': 13, 'E': 14, 'F' : 15}   #16진수 딕셔너리

    result = ''
    for char in hex:    #16진수 각 자리가 2진수 4자리로 변환된다
        if char.isdigit() == False: #A ~ F: 11 ~ 16
            num = hex_dict[char]
        else:
            num = int(char)

        bin = ''  # 변환한 2진수 담을 변수
        while num >= 1:    #2진수 변환
            bin = str(num % 2) + bin
            num = num // 2
        while len(bin) < 4: #16진수 각 자리는 2진수 4자리
            bin = '0' + bin
        result += bin

    print(f'#{tc} {result}')