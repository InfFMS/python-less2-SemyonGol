print('Enter first interval:')
a1 = int(input())
b1 = int(input())
print('Enter coordinates of needed position in format (x,y):')
a2 = int(input())
b2 = int(input())
if a1 >= a2 and b1 <= b2:
    print('[', a1, '; ' ,b1, ']', sep='')
elif a1 >= a2 and b1 >= b2:
    print('[', a1, '; ' ,b2, ']', sep='')
elif a1 <= a2 and b1 <= b2:
    print('[', a2, '; ' ,b1, ']', sep='')
elif a1 > b2 or a2 > b1:
    print('E')
