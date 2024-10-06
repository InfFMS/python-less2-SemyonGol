
n = int(input())
if n > 12 or n < 0:
    print('Error')
else:
    if n == 1:
        a = 'Январь'
    elif n == 2:
        a = 'Февраль'
    elif n == 3:
        a = 'Март'
    elif n == 4:
        a = 'Апрель'
    elif n == 5:
        a = 'Май'
    elif n == 6:
        a = 'Июнь'
    elif n == 7:
        a = 'Июль'
    elif n == 8:
        a = 'Август'
    elif n == 9:
        a = 'Сентябрь'
    elif n == 10:
        a = 'Октябрь'
    elif n == 11:
        a = 'Ноябрь'
    elif n == 12:
        a = 'Декабрь'
    print('Сейчас:', a)