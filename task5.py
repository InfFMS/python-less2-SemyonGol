p = 0
for i in range(10000, 100000):
    if i%133 == 125 and i%134 == 111:
        p +=1
        print(p,': ', i, sep='')