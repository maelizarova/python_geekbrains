delete = ['(л)', '(лаб)', '(пр)', ':', '—', '.']
lessons = {}
with open("in6.txt", "r", encoding= 'utf-8') as f:
    for line in f:
        for part in delete:
            line = line.replace(part, ' ')
        line = line.split()
        lessons.update({line[0]: sum(int(l) for l in line[1:])})
print(lessons)
