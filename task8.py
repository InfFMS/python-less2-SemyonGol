print('Enter coordinates of bishop in format (x,y):')
x1 = int(input())
y1 = int(input())
if (x1 < 0 or y1 < 0) or (x1 > 8 or y1 > 8):
    print('Invalid coordinates! (Choose from 1 to 8)')
else:
    print('Enter coordinates of needed position in format (x,y):')
    x2 = int(input())
    y2 = int(input())
    if (x2 < 0 or y2 < 0) or (x2 > 8 or y2 > 8):
        print('Invalid coordinates! (Choose from 1 to 8)')
    else:
        if abs(x1-x2) == abs(y1-y2):
            print('Bishop can get to that coordinates')
        else:
            print('Bishop can\'t get to that coordinates')