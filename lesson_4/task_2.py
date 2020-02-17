my_list = [10, 2, 25, 30, 15, 50, 86, 1]
new_list = [my_list[ind + 1] for ind in range(len(my_list) - 1) if my_list[ind] < my_list[ind + 1]]
print(new_list)
