from random import randint


def min_max(a):
    min = a[0]
    max = a[0]
    for i in a:
        if i < min:
            min = i
        elif i > max:
            max = i
    return min, max


b = []
n = int(input('Enter size of list: '))
for i in range(n):
    b.append(randint(0, 100))
print(b)

c = min_max(b)
for i in range(len(c)):
    if i == 0:
        print('min value of list =', c[i])
    else:
        print('max value of list =', c[i])
