def shape_dict(temp, dict): #딕셔너리에 그림의 도형 개수 입력
    for i in range(len(temp)):
        if i != 0:
            if temp[i] == 1:
                dict['triangle'] += 1
            elif temp[i] == 2:
                dict['square'] += 1
            elif temp[i] == 3:
                dict['circle'] += 1
            else:
                dict['star'] += 1

def winner(a_dict, b_dict): #이긴쪽 리턴, 비기면 D리턴
    if a_dict['star'] > b_dict['star']:
        return 'A'
    elif a_dict['star'] < b_dict['star']:
        return 'B'
    else:
        if a_dict['circle'] > b_dict['circle']:
            return 'A'
        elif a_dict['circle'] < b_dict['circle']:
            return 'B'
        else:
            if a_dict['square'] > b_dict['square']:
                return 'A'
            elif a_dict['square'] < b_dict['square']:
                return 'B'
            else:
                if a_dict['triangle'] > b_dict['triangle']:
                    return 'A'
                elif a_dict['triangle'] < b_dict['triangle']:
                    return 'B'
                else:
                    return 'D'

N = int(input())    #총 라운드 수
for i in range(N):
    a_dict = {'star': 0, 'circle': 0, 'square': 0, 'triangle': 0}  # a카드 딕셔너리
    b_dict = {'star': 0, 'circle': 0, 'square': 0, 'triangle': 0}  # b카드 딕셔너리
    temp1 = list(map(int, input().split()))  #0인덱스 그림 총 개수, 1~ 삼각,사각,원,별
    temp2 = list(map(int, input().split()))

    shape_dict(temp1, a_dict)
    shape_dict(temp2, b_dict)

    result = winner(a_dict, b_dict)
    print(result)