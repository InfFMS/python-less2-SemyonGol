p = 0
for i in range(100, 1000):
    a = i//100
    b = (i%100)//10
    c = i%10
    if a**3 + b**3 + c**3 == i:
        p += 1
        print(p, ': ', i, sep='')