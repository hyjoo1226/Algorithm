y = int(input())

def yoon(y):
    if y % 100 == 0 and y % 400 != 0:
        return False
    if y % 4 != 0:
        return False
    return True

if yoon(y) == True:
    print("true")
else:
    print("false")