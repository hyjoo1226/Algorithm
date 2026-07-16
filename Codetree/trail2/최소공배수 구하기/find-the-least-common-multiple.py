n, m = map(int, input().split())

# Please write your code here.
def mm(n, m):
    for i in range(1, 10001):
        if i % n == 0 and i % m == 0:
            print(i)
            break

mm(n, m)