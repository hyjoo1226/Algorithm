def req(D):
    return req(D - 1) + req(D - 2)

D, K = map(int, input().split())    #날 D, 그 날 준 떡 개수 K

A = 0   #첫째날
B = 0   #둘째날

req(0)  #재귀함수 피보나치

