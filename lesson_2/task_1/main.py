a = [1, 10]
data = [1, '1', {'one': 1, 'two': 10}, (1, 10), set(a)]
for el in data:
    print(f'Type of element {el} in data is {type(el)}')

