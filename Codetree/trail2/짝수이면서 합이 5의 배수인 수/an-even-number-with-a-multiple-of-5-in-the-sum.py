def mm(n):
    str_n = str(n)
    if n % 2 == 0 and (int(str_n[0]) + int(str_n[1])) % 5 == 0:
        print("Yes")
    else:
        print("No")       

n = int(input())
mm(n)