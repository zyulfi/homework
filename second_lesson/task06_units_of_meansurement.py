#Задача 6
#Потребител въвежда от клавиатурата броя на метрите.
#Изходът трябва да е резултат от преобразуването на метрите в сантиметри, дециметри, милиметри и мили.

meters = float(input("Моля, въведете броя на метрите: "))

centimeters = meters * 100
decimeters = meters * 10
millimetres = meters * 1000
miles = meters * 1610

print("Тhe entered " + str(meters) + " meters are:" + "\n"
      + str(centimeters) + " centimeters" "\n"
      + str(decimeters) + " decimeters" "\n"
      + str(millimetres) + " millimeters" "\n"
      + str(miles) + " miles")