#Задача 1
#Потребител въвежда три цифри от клавиатурата.
# Трябва да се генерира число, което съдържа тези цифри.
# Например, ако от клавиатурата са въведени 1, 5 и 7, трябва да се генерира числото 157.


num_first = input("Please enter first number: ")
num_second = input("Please enter second number: ")
num_third = input("Please enter third number: ")

while True:
    if num_first.isdigit() and num_second.isdigit() and num_third.isdigit():
        print("The generated number is: " + str(num_first) + str(num_second) + str(num_third))
        break
    else:
        print("The numbers entered must be integers.")
        if not num_first.isdigit():
            num_first = input("Enter an integer for first number: ")
        if not num_second.isdigit():
            num_second = input("Enter an integer for second number: ")
        if not num_third.isdigit():
            num_third = input("Enter an integer for third number: ")