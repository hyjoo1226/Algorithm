#27866 문자와 문자열
S = input()
i = int(input())
print(S[i - 1])

#2743 단어 길이 재기
S = input()
print(len(S))

#9086 문자열
T = int(input())
for i in range(T):
    S = input()
    if len(S) == 1:
        print(S + S)
    else:
        print(S[0] + S[-1])

#11654 아스키 코드
S = input()
print(ord(S))

#11720 숫자의 합
N = int(input())
S = input()
sum = 0

for i in S:
    sum += int(i)
print(sum)

#10809 알파벳 찾기

#2675 문자열 반복
T = int(input())
for i in range(T):
    R, S = input().split()
    R = int(R)
    for  str in S:
        print(str * R, end = "")
    print("")

#1152 단어의 개수
S = list(input().split())
print(len(S))

#2908 상수

#5622 다이얼

#11718 그대로 출력하기