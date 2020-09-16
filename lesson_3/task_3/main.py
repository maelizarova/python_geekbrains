def my_func(a, b, c):
    if c <= a and c <= b:
        return a + b
    elif a >= b:
        return c + a


a, b, c = map(int, input().split())
print(my_func(a, b, c))