total_3 = 0
total_5 = 0

for i in range(10):
    n = int(input())
    if n % 3 == 0:
        total_3 += 1
    
    if n % 5 == 0:
        total_5 += 1

print(total_3, total_5)