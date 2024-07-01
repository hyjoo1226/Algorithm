#1330 두 수 비교하기
A, B = input().split()
A = int(A)
B = int(B)

if A > B:
    print(">")
elif A < B:
    print("<")
if A == B:
    print("==")

#9498 시험 성적
grade = int(input())

if grade >= 90 and grade <= 100:
    print("A")
elif grade >= 80 and grade <= 89:
    print("B")
elif grade >= 70 and grade <= 79:
    print("C")
elif grade >= 60 and grade <= 69:
    print("D")
else:
    print("F")

#2753 신년
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("1")
else:
    print("0")

#14681 사분면 고르기
X = int(input())
Y = int(input())

if X > 0:
    if Y > 0:
        print("1")
    else:
        print("4")
else:
    if Y > 0:
        print("2")
    else:
        print("3")

#2884 알람 시계
H, M = input().split()
H = int(H)
M = int(M)

if M >= 45:
    print(H, M - 45)
else:
    if H == 0:
        H = 24
    print(H - 1, M + 15)

#2525 오븐 시계
A, B = input().split()
C = input()
hour = int(A)
minute = int(B) + int(C)

while minute >= 60:
    minute = minute - 60
    hour = hour + 1

if hour >= 24:
    hour = hour - 24

print(hour, minute)

#2480 주사위 세개
# a = list(map(int, input().split()) 입력값 정수형 리스트로 받기

dice = list(map(int, input().split()))
dice.sort()
dice.reverse()

if dice[0] == dice[1]:
    if dice[0] == dice[2]:
        prize = 10000 + dice[0] * 1000
    else:
        prize = 1000 + dice[0] * 100
else:
    if dice[1] == dice[2]:
        prize = 1000 + dice[1] * 100
    else:
        prize = dice[0] * 100

print(prize)