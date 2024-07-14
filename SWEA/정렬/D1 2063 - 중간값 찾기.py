# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QPsXKA2UDFAUq
# 문자열을 정수형으로 새 리스트 만들기: N_list = [int(i) for i in temp]

N = input()
temp = list(input().split())
N_list = [int(i) for i in temp]
N_list.sort()
a = int(N) // 2
print(N_list[a])