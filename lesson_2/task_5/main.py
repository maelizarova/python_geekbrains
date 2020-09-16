my_list = [7, 5, 3, 3, 2]
new_el = int(input('Please, enter a new rating: '))
while new_el != 0:
    for ind in range(len(my_list)):
        if my_list[ind] < new_el:
            my_list.insert(ind, new_el)
            break
    if new_el not in my_list:
              my_list.append(new_el)
    new_el = int(input('Please, enter a new rating: '))
print(my_list)

