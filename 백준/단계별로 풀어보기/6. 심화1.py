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
#별 뒤쪽은 출력 없음
N = int(input())
for i in range(2 * N - 1):
    if i < N:
        print(' ' * (N - i - 1) + '*' * (2 * i + 1))
    else:
        print(' ' * (i - N + 1) + '*' * (4 * N - 2 * i - 3))
        
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
S = input()
alpha = {}

for char in S.upper():
    if alpha.get(char) == None:
        alpha.setdefault(char, 1)
    else:
        alpha[char] += 1
number = 0

for i in alpha.values():
    if number == 0:
        number = i
    if number < i:
        number = i

answer = [k for k, v in alpha.items() if v == number]

if len(answer) == 1:
    print(answer[0])
else:
    print('?')

#2941 크로아티아 알파벳
string = input()
count = 0

def croalpha(string, alpha):
    global count
    new_string = string.split(alpha)
    if len(new_string) != 1:
        number = len(new_string) - 1
        count += number

croalpha(string, 'c=')
croalpha(string, 'c-')
croalpha(string, 'dz=')
croalpha(string, 'd-')
croalpha(string, 'lj')
croalpha(string, 'nj')
croalpha(string, 's=')
croalpha(string, 'z=')

print(len(string) - count)

#1316 그룹 단어 체커
N = int(input())
count = 0

for i in range(N):
    S = input()
    new_lst = []
    temp = ''
    checker = 0
    for item in S:
        if temp != item:
            temp = item
            new_lst.append(item)
            if new_lst[-1] in new_lst[:-1]:
                checker = 1
                break
    if checker == 0:
        count += 1

print(count)

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