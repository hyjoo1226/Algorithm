a, b = map(int, input().split())

# Please write your code here.
def ss(a, b):
    total = 0
    for i in range(a, b + 1):
        if i % 3 == 0:
           total += 1
        else:
            str_num = str(i)
            for j in range(len(str_num)):
                if int(str_num[j]) in [3, 6, 9]:
                    total += 1
                    break
    return total

print(ss(a, b))
