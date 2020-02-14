def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Division by zero'
