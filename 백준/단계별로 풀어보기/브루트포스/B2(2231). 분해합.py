N = int(input())

result = 0

for i in range(1, N):
    digit = str(i)
    if N == i + sum(map(int, digit)):
        result = i
        break
    
print(result)