a, b, c, d, e ,f = map(int, input().split())

y = int((c * d - a * f) / (b * d - a * e))
x = int((c * e - b * f) / (a * e - b * d))
print(x, y)