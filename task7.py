q = 0
b = True
print('Enter limit number:', end=' ')
N = int(input())
for i in range(2, N+1):
    for p in range(2, i):
        if i%p == 0:
            b = False
    if b:
        q += 1
        print(q, ': ', i, sep='')
    b = True
