from itertools import count, cycle

n = int(input('Введите начальное значение: '))
for el in count(n):
    if el > n + 10:
        break
    else:
        print(el)


с = 0
for el in cycle("Red, Orange, Yellow, Green, Blue, Indigo, Violet"):
    if с > 10:
        break
    print(el)
    с += 1