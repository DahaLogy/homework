print('Hi, please enter 2 numbers a and b :')
a = input('number a:')
b = input('number b:')


def is_number(a, b):
    try:
        float(a), float(b)
        return True
    except ValueError:
        return False


if True:
    a = float(a)
    b = float(b)

operator = ['|x|', 'int x', 'float x', 'x^y', 'round x', 'x+y', 'x-y', 'x*y', 'x/y ', 'complex']
operation = input('>>')

if operation not in operator:
    print('ERROR!\nchoose correct operation :', operator)
    operation = input('>>')
else:
    pass
# import math

if operation == operator[0]:
    x = input(print('choose number : a or b: '))
    if x == 'a':
        a = float(a)
        if a < 0:
            print(a * (-1))
    print(a)
    if x == 'b':
        b = float(b)
        if b < 0:
            print(b * (-1))
    print(b)
elif operation == operator[1]:
    x = input(print('choose number : a or b: '))
    if x == 'a':
        print(int(a))
    if x == 'b':
        print(int(b))
elif operation == operator[2]:
    x = input(print('choose number : a or b: '))
    if x == 'a':
        print(float(a))
    if x == 'b':
        print(float(b))
elif operation == operator[3]:
    print(a ** b)
elif operation == operator[4]:
    x = input(print('choose number : a/b: '))
    if x == 'a':
        print(round(a))
    if x == 'b':
        print(round(b))
elif operation == operator[5]:
    print(a + b)
elif operation == operator[6]:
    print(a - b)
elif operation == operator[7]:
    print(a * b)
elif operation == operator[8]:
    print(a / b)
elif operation == operator[9]:
    print(complex(re=a))
