def token_num(token, card, i):
    for j in range(7):
        if card[i] == j:
            token[j] += 1

def is_neighbor(i):
    if (card[reverse_dict[i] + 1] != 0 and card[reverse_dict[i] + 2] != 0) or \
        (card[reverse_dict[i] + 1] != 0 and card[reverse_dict[i] - 1] != 0) or \
        (card[reverse_dict[i] - 1] != 0 and card[reverse_dict[i] - 2] != 0):
        return 1
    else:
        return 0
    
T = int(input())
for test_case in range(1, T + 1):
    temp = input()  #카드 6장 넣기
    card = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}   #0~9카드 딕셔너리
    for item in temp:   #딕셔너리에 카드6장 넣어줌
        card[int(item)] += 1
    
    token = [0, 0, 0, 0, 0, 0, 0]   
    for i in range(10):
        token_num(token, card, i)
        #6장 - token[6] = 1                                 tripet/tripet
        #4장,1장,1장 - token[4] = 1, token[1] = 2           tripet/run or x 
        #3장,3장 - token[3] = 2                             tripet/tripet
        #3장,1장,1장,1장 - token[3] = 1, token[1] = 3       tripet/run or x
        #2장,2장,2장 - token[2] = 3                         run/run or x
        #1장,1장,1장,1장,1장,1장 - token[1] = 6              run/run or x

    result = 0
    reverse_dict = {v:k for k,v in card.items()}    #key,value값 뒤집은 card딕셔너리
    print(token)
    if token[6] == 1:
        result = 1
    if (token[4] == 1) and (token[1] == 2):
        result = is_neighbor(4)                     #tripet인 경우 1 반환
    if token[3] == 2:
        result = 1
    if (token[3] == 1) and (token[1] == 3):
        result = is_neighbor(1)
    if token[1] == 6:
        count = 0
        for i in range(10):
            if card[i] == 1:
                result = is_neighbor[i]
                # print(f'asd: {result}')
            if (result == 1) and (card[i] == 0):
                count = 1
            if (count == 1) and (card[i] == 1):
                result = is_neighbor[i]
                break

    print(f'#{test_case} {result}')