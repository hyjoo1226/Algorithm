n, m = map(int, input().split())

# Please write your code here.
def num(n, m):
    a = 0
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
    
    lst2 = []
    for ls in lst:
        if m % ls == 0:
            lst2.append(ls)

    print(lst2[-1])

num(n, m)