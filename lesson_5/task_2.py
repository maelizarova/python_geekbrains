with open("out2.txt", "r", encoding= 'utf-8') as f:
    ind = 0
    for line in f:
        print(len(line.split()))
        ind += 1
    print(f'Всего строк: {ind}')