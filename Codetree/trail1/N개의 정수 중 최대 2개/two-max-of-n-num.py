n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
for i in range(n):
    for j in range(i, n):
        if j + 1 >= n:
            continue
        if a[i] < a[j + 1]:
            temp = a[i]
            a[i] = a[j + 1]
            a[j + 1] = temp
print(a[0], a[1])