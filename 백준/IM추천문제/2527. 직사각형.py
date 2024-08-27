for i in range(4):
    square = list(map(int, input().split()))
    result = 0
    square_one = square[:4]
    square_two = square[4:]

    if square_one[2] < square_two[0] or square_one[0] > square_two[2] or \
        square_one[3] < square_two[1] or square_one[1] > square_two[3]:
        result = 'd'

    elif (square_one[0] == square_two[2] and square_one[1] == square_two[3]) or \
            (square_one[0] == square_two[2] and square_one[3] == square_two[1]) or \
            (square_one[2] == square_two[0] and square_one[1] == square_two[3]) or \
            (square_one[2] == square_two[0] and square_one[3] == square_two[1]):
            result = 'c'

    elif square_one[2] == square_two[0] or square_one[0] == square_two[2] or \
        square_one[3] == square_two[1] or square_one[1] == square_two[3]:
        result = 'b'

    else:
        result = 'a'

    print(result)