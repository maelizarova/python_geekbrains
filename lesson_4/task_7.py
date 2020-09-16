def fact_gen():
    fact = 1
    for el in range(1, 15):
        fact = fact * el
        yield fact


for el in fact_gen():
    print(el)