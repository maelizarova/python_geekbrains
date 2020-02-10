seasons_as_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], 'fall', 'summer', 'spring', 'winter']
seasons_as_dict = {(12, 1, 2): 'winter', (3, 4, 5): 'spring', (6, 7, 8): 'summer', (9, 10, 11): 'fall'}
month = int(input('Please, enter the number of month: '))
#     первый вариант для списка:
for idx in range(len(seasons_as_list) // 2):
    try:
        season = seasons_as_list[idx].index(month)
        print(seasons_as_list[-season])
    except ValueError:
        continue
#     второй вариант для списка:
for idx in range(len(seasons_as_list) // 2):
    if month in seasons_as_list[idx]:
            print(seasons_as_list[-(idx + 1)])
for key in seasons_as_dict:
    if month in key:
        print(seasons_as_dict.get(key))