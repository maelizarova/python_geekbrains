def my_func(x, y):
    ans = 1
    for power in range(abs(y)):
        ans = ans / x
    return ans


print(my_func(5, -2))