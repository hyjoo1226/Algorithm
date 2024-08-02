import sys
sys.stdin = open("GNS_test_input.txt", "r")

T = int(input())

for i in range(1, T + 1):
    num, tc_len = input().split()
    tc_len = int(tc_len)
    str_lst = list(input().split())
    #각 숫자의 개수를 카운트하는 딕셔너리 planet 0값으로 초기화
    planet = {'ZRO':0, 'ONE':0, 'TWO':0, 'THR':0, 'FOR':0, 'FIV':0, 'SIX':0, 'SVN':0, 'EGT':0, 'NIN':0}
    for item in str_lst:    #리스트의 아이템(숫자)가 나타날때마다 해당 키의 밸류값 1 증가
        planet[item] += 1
    
    print(num)
    for k,v in planet.items():
        for _ in range(v):
            print(k, end=' ')
    print()