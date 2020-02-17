my_list = [10, 12, 25, 1, 30, 15, 15, 50, 12, 1]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)