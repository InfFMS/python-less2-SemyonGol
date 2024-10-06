b = True
y = int(input())
if y > 120 or y < 0:
    print('Недопустимое значение')
    b = False
if y > 10 and y < 20:
    print('Вам', y, "лет")
    b = False
if b == True:
    y = str(y)
    if y[-1] == '1':
        a = 'год'
    elif (y[-1] == '2') or (y[-1] == '3') or (y[-1] == '4'):
        a = 'года'
    else:
        a = 'лет'
    print('Вам', y, a)