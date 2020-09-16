vocabulary = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
with open('in4.txt', 'r', encoding='utf-8') as f_1:
    with open('out4.txt', 'w', encoding='utf-8') as f_2:
        for line in f_1:
            line = line.split()
            line[0] = vocabulary.get(line[0])
            new_line = (l + ' ' for l in line)
            f_2.writelines(new_line)
            f_2.write('\n')
