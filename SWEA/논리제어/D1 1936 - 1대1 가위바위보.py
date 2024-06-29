# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PjKXKALcDFAUq
#예외처리 해야함

a, b = input().split()
if a == b:
    print("다시 입력해주세요")
else:
    result = 'A'
    if (a == '3' and b == '1') or (a == '2' and b == '3') or (a == '1' and b == '2'):
        result = 'B'
    print(result)