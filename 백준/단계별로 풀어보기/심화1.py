#25083 새싹
print('         ,r\'\"7')
print("r`-_   ,'  ,/")
print(' \. ". L_r\'')
print('   `~\\/')
print('      |')
print('      |')

#3003 킹, 퀸, 룩, 비숍, 나이트, 폰
def chess_count(piece, count):
    sub = count - piece
    return (sub)

king, queen, rook, bishop, knight, pawn = map(int, input().split())
print(chess_count(king, 1),end = " ")
print(chess_count(queen, 1),end = " ")
print(chess_count(rook, 2),end = " ")
print(chess_count(bishop, 2),end = " ")
print(chess_count(knight, 2),end = " ")
print(chess_count(pawn, 8),end = " ")

#2444 별 찍기 - 7

#10988 팰린드롬인지 확인하기
str = input()
checker = 0
token = 1
if len(str) % 2 == 0:
    checker = len(str) / 2
else:
    checker = len(str) // 2
i = -1
for s in str:
    if s != str[i]:
        token = 0
    if abs(i) == checker:
        break
    i -= 1
print(token)

#1157 단어 공부

#2941 크로아티아 알파벳

#1316 그룹 단어 체커

# 25206 너의 평점은
def grade_cvt(grade):
    if grade == 'A+':
        return (4.5)
    elif grade == 'A0':
        return (4.0)
    elif grade == 'B+':
        return (3.5)
    elif grade == 'B0':
        return (3.0)
    elif grade == 'C+':
        return (2.5)
    elif grade == 'C0':
        return (2.0)
    elif grade == 'D+':
        return (1.5)
    elif grade == 'D0':
        return (1.0)
    else:
        return (0.0)
    
point_sum = 0
grade_sum = 0

for i in range(20):
    lecture, point, grade = input().split()
    if grade == 'P':
        continue
    else:
        point_sum += float(point)
        grade_sum += float(point) * grade_cvt(grade)
print(grade_sum / point_sum)