n = int(input())

# Please write your code here.
def a(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    s = s // 10
    return s

print(a(n))