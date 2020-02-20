f = open("out1.txt", "w")
line = input('Введите содержимое файла: ')
while line != '':
    f.write(line)
    line = input()
f.close()