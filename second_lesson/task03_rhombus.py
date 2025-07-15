#Задача 3
#Напишете програма, която пресмята площта на ромб.
#Потребителят въвежда от клавиатурата дължините на двата диагонала на ромб.

first_diagonal = float(input("Please enter the length of the first diagonal of the rhombus: "))
second_diagonal = float(input("Please enter the length of the second diagonal of the rhombus: "))

area_rombus = first_diagonal * second_diagonal / 2

print("The area of the rhombus is: " + str(area_rombus))