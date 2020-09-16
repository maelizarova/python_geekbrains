data = list(input('Please, enter the elements of new list: ').split())
iteration =  len(data) - 1 if len(data) // 2 == 0 else len(data) - 2
for idx in range(0, iteration, 2):
    data[idx], data[idx + 1] = data[idx + 1], data[idx]
print(data)