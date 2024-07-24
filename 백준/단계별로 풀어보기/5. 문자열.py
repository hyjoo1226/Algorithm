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
S = input()
alpha = list(range(26))
temp = 'a'
count = 0

for i in alpha:
    alpha[i] = -1
for str in S:
    if alpha[ord(str) - ord(temp)] != -1:
        pass
    else:
        alpha[ord(str) - ord(temp)] = count
    count += 1
for i in alpha:
    print(i, end = " ")

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
A, B = input().split()
A_r = ''
B_r = ''
for i in A:
    A_r = i + A_r
for i in B:
    B_r = i + B_r
if int(A_r) > int(B_r):
    print(A_r)
else:
    print(B_r)
    
#5622 다이얼
#모든 범위를 다 직접 입력한거라 더 이쁜 코드가 없을까 아쉬움
S = input()
num = 0
sum = 0

for str in S:
    if str >= 'A' and str <= 'C':
        num = 2
    elif str >= 'D' and str <= 'F':
        num = 3
    elif str >= 'G' and str <= 'I':
        num = 4
    elif str >= 'J' and str <= 'L':
        num = 5
    elif str >= 'M' and str <= 'O':
        num = 6
    elif str >= 'P' and str <= 'S':
        num = 7
    elif str >= 'T' and str <= 'V':
        num = 8
    elif str >= 'W' and str <= 'Z':
        num = 9
    else:
        num = 1 
    sum += num  
print(len(S) + sum)

#11718 그대로 출력하기
#입력값이 없을때 - EOF Error(End of File Error)
while True:
    try:
        print(input())
    except:
        break