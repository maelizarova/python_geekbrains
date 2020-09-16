num = input('Введите числа в файл: ')
with open('out5.txt', 'w', encoding='utf-8') as f:
    while num:
        f.write(f'{num} ')
        num = input()

with open('out5.txt', 'r', encoding='utf-8') as f:
    nums = map(int, f.readline().split())
    print(sum(nums))