#2557 hello world!
print("Hello World!")

#1000 A+B
A,B = input().split()
print(int(A)+int(B))

#1001 A-B
A,B = input().split()
print(int(A)-int(B))

#10998 A*B
A,B = input().split()
print(int(A)*int(B))

#1008 A/B
A,B = input().split()
print(int(A)/int(B))

#10869 사칙연산
A,B = input().split()
A = int(A)
B = int(B)
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)

#10926 ??!
A = input()
print(A + "??!")

#18108 1998년생인 내가 태국에서는 2541년생?!
A = input()
print(int(A) - 543)

#10430 나머지
A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)

#2588 곱셈
A = input()
B = input()
B_list = list(B)
B_list.reverse()

for i in B_list:
    print(int(A) * int(i))
print(int(A)*int(B))

#11382 꼬마 정민
A, B, C = input().split()
print(int(A) + int(B) + int(C))

#10171 고양이
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")

#10172 개
print("|\\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print("||_/=\\\\__|")