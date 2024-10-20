n = 0
temp = 0
while True:
    if n == 0:
        a = float(input('Enter first operand: '))
        x = input('Enter operation: ')
        b = float(input('Enter second operand: '))
        if(x == '+'):
            n = a + b
            print(a, '+', b, '=', n)
        elif(x == '-'):
            n = a - b
            print(a, '-', b, '=', n)
        elif(x == '*'):
            n = a * b
            print(a, '*', b, '=', n)
        elif(x == '/'):
            n = a / b
            print(a, '/', b, '=', n)
        elif(x == '//'):
            n = a // b
            print(a, '//', b, '=', n)
        else:
            print('Incorrect operator, try again!')
            continue
    else:
        y = input('Enter operation: ')
        if(y in ['+', '-', '*', '/', '//']):
            c = float(input('Enter operand: '))
            if(y == '+'):
                n1 = n
                n = n + c
                print(n1, '+', c, '=', n)
            elif(y == '-'):
                n1 = n
                n = n - c
                print(n1, '-', c, '=', n)
            elif(y == '*'):
                n1 = n
                n = n * c
                print(n1, '*', c, '=', n)
            elif(y == '/'):
                n1 = n
                n = n / c
                print(n1, '/', c, '=', n)
            elif(y == '//'):
                n1 = n
                n = n // c
                print(n1, '//', c, '=', n)
        elif(y == 'End'):
            temp = 1
        else:
            print('Incorrect operator, try again!')
    if(temp == 1):
        print('Result =', n)
        break
    else:
        continue
        
