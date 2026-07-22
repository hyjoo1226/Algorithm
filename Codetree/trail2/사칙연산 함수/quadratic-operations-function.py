a, o, c = input().split()
a = int(a)
c = int(c)

def calculator(a, o, c):
    if o == '+':
        print(f'{a} {o} {c} = {a + c}')
    elif o == '-':
        print(f'{a} {o} {c} = {a - c}')
    elif o == '*':
        print(f'{a} {o} {c} = {a * c}')
    elif o == '/':
        print(f'{a} {o} {c} = {int(a / c)}')
    else:
        print(False)

calculator(a, o, c)