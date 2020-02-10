goods = {}
result_goods = []
print('Добавление нового товара начинать с характеристики "название".')
print('Для окончания ввода, введите "0 0".')
print('Введите название храктеристики товара, затем ее значение через пробел: ')
characteristic, value = input().split()
flag = 0
while (characteristic, value) != ('0', '0'):
    if characteristic == 'название' and flag:
        result_goods.append(goods)
        goods = {}
    goods.update({characteristic:value})
    flag = 1
    characteristic, value = input().split()
result_goods.append(goods)
result_goods = list(enumerate(result_goods, 1))
goods_keys = goods.keys()
new_goods = {}
for g_key in goods_keys:
    new_goods.setdefault(g_key, [])
    for ind in range(len(result_goods)):
        value = result_goods[ind][-1].get(g_key)
        if value not in new_goods[g_key]:
            new_goods[g_key].append(value)
print(new_goods)