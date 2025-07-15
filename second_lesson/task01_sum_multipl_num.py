# Задача 1
# Потребител въвежда три числа от клавиатурата. Трябва да се намери сумата на числата и произведението
# на числата.
# Резултатът от изчисленията трябва да се изведе на екрана.

num_one = float(input("Please, enter first number: "))
num_second = float(input("Please, enter second number: "))
num_third = float(input("Please, enter third number: "))

num_sum = num_one + num_second + num_third
num_multiplication = num_one * num_second * num_third

print("The sum of the three numbers is: " + str(num_sum))
print("The multiplication of the three numbers is: " + str(num_multiplication))