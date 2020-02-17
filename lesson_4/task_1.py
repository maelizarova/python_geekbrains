import sys

def my_func(*args):
    return args[0] * args[1] + args[2]


# print(sys.argv)

if len(sys.argv) == 3:
    try:
        result = int(sys.argv[0]) * int(sys.argv[1]) + int(sys.argv[2])
    except ValueError:
        print('Введены неверные данные')
else:
    print('Введите выработку в часах, ставку в час и премию:')
    nums = list(map(int, input('').split()))

print(f'Заработная плата сотрудника: {my_func(*map(float, nums))}')
