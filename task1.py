
n = int(input())
if n == 1:
    a, b = '8.30', '9.15'
elif n == 2:
    a, b = '9.25', '10.10'
elif n == 3:
    a, b = '10.20', '11.05'
elif n == 4:
    a, b = '11.15', '12.00'
elif n == 5:
    a, b = '12.30', '13.05'
elif n == 6:
    a, b = '13.15', '14.10'
else:
    a, b = 'E', 'E'
print("Начало урока: %(time1)s; Окончание: %(time2)s" % {'time1': a, 'time2': b})