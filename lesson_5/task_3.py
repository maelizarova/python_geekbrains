summa = 0
ind = 0
with open("out3.txt", "r", encoding= 'utf-8') as f:
    for line in f:
        worker = line.split()
        ind += 1
        if int(worker[1]) < 20000:
            print(worker[0])
        summa += int(worker[1])
    print(f'Средняя величина дохода: {summa / ind}')
