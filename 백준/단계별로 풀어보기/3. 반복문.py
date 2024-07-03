#2739 구구단
N = int(input())

for i in range(1, 10):
    print(N, "*", i, "=", N * i)

#10950 A+B-3
T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(A + B)

#8393 합
n = int(input())
sum = 0

for i in range(n + 1):
    sum = sum + i
print(sum)

#25304 영수증
X = int(input())
N = int(input())
sum = 0

for i in range(N):
    a, b = map(int, input().split())
    sum = sum + a * b
if X == sum:
    print("Yes")
else:
    print("No")

#25314 코딩은 체육과목 입니다
N = int(input())
long = N // 4

if N % 4 != 0:
    long = long + 1
for i in range(long):
    print("long", end =" ")
print("int")

#15552 빠른 A+B
import sys

T = int(input())
5
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)

#11021 A+B-7
import sys

T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #%d: %d" % (i + 1, A + B))

#11022 A+B-8
import sys

T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #%d: %d + %d = %d" % (i + 1, A, B, A + B))

#2438 별 찍기 1
N = int(input())

for i in range(N):
    print("*" * (i + 1))

#2439 별 찍기 2
N = int(input())

for i in range(N):
    print(" " * (N - 1 - i) + "*" * (i + 1))

#10952 A+B-5
import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    if (A == 0 and B == 0):
        break
    print(A + B)

#10951 A+B-4
import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)
    except:
        break