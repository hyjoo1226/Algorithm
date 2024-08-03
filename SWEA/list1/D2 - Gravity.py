T = int(input())

for test_case in range(1 , T + 1):
    width = int(input())    #가로의 길이
    box_lst = list(map(int, input().split()))   #쌓여있는 상자의 수 리스트
    result = 0  #낙차

    highest_box = 0    #가장 높은 박스
    for item in box_lst:
        if highest_box < item:
            highest_box = item
    
    for i in range(highest_box):    #회전했을 때 가장 긴 가로값까지 순회
        

