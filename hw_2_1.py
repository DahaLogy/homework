print('enter 2 numbers a and b : ')
isNum = True
# A
a = (input('a :'))  # this value for a different input a

z = str  # for our number a
print('a[0] is: ', a[0])
if a[0] == '-':
    z = a
    a = a.replace('-', '')
else:
    z = a

while a.isdecimal() != isNum or a.isdigit() != isNum:
    print('ERROR, input number')
    a = (input('a :'))
    if a[0] == '-':
        z = a
        a = a.replace('-', '')
        print('a is: ', a)
    else:
        z = a
        # print('z is: ', z)
z = int(z)

# B
b = (input('b :'))  # this value for a different input b
k = str    # for our number b
# print('b[0] is: ', b[0])
if b[0] == '-':
    k = b
    b = b.replace('-', '')
else:
    k = b
while b.isdecimal() != isNum or b.isdigit() != isNum:
    print('ERROR, input number b:')
    # b = (input('b :'))
    if b[0] == '-':
        k = b
        b = b.replace('-', '')
        print('b is: ', b)
    else:
        k = b
        print('k is: ', k)
k = int(k)
if z < 0 and k < 0:
    print('There is no natural numbers.')
if z > k:
    y = k
    k = z
    z = y
k -= 1
arr = []
sum_nature_num = 0
z -= 1
while z <= k:
    z += 1
    if z > 0:
        arr.append(z)
        sum_nature_num += z
print('Natural numbers:\n', arr)
print('Sum of natural numbers is: ', sum_nature_num)
