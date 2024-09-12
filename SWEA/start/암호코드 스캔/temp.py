def hex_bin(char):  #16진수 2진수 변환
    hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}  # 16진수 딕셔너리
    result = ''
    if char.isdigit() == False:  # A ~ F: 11 ~ 16
        num = hex_dict[char]
    else:
        num = int(char)

    bin = ''  # 변환한 2진수 담을 변수
    while num >= 1:  # 2진수 변환
        bin = str(num % 2) + bin
        num = num // 2
    while len(bin) < 4:  # 16진수 각 자리는 2진수 4자리
        bin = '0' + bin

    result += bin
    return result

a = '02F5E65BA316BD78'
b = '01DB176C588D26EC'
temp1 = []
for i in range(15, -1, -1):
    temp1.append(hex_bin(a[i]))
    # print(temp)
    # for j in range(3, -1 ,-1):
    #     temp1.append(temp[j])
print(temp1)
# ['1000', '0111', '1101', '1011', '0110', '0001', '0011', '1010', '1011', '0101', '0110', '1110', '0101', '1111', '0010', '0000']    a 두번쨰
# ['1110', '0110', '0010', '1101', '1000', '1000', '0101', '1100', '0110', '0111', '0001', '1011', '1101', '0001', '0000']    b   첫번쨰