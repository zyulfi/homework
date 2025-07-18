#Задача 4
#Напишете програма, която пресмята площта на триъгълник.
#Потребителят въвежда от клавиатурата размера на основата на триъгълника и размера на височината.

base = float(input("Please enter the base of the triangle: "))
height = float(input("Please enter the height of the triangle: "))
face_triangle = (base * height) / 2

print("The area of the triangle is: " + str(face_triangle))