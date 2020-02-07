sec = int(input("Please, enter the number of seconds passed: "))
print("Formatted time: {}:{}:{}.".format(sec // 3600, sec % 3600 // 60 , sec % 3600 % 60))