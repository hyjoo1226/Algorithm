Y = int(input())

if Y % 4 != 0:
    print("false")
elif (Y % 100 == 0 and Y % 400 != 0):
    print("false")
else:
    print("true")