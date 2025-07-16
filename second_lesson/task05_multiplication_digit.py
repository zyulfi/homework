#Задача 5
#Потребител въвежда от клавиатурата число , състоящо се от четири цифри.
# Трябва да се намери произведението на цифрите. Например, ако от клавиатурата е въведено числото 1324,
# резултатът от произведението на числата е 1*3*2*4 = 24.

thousands = int(input("Please enter a four-digit integer: "))

num_thousands = int((thousands - (thousands % 1000)) / 1000) # I'm taking the thousandths
hundreds = thousands % 1000
num_hundreds = int((hundreds - (hundreds % 100)) / 100) # I'm taking the hundreds
dozens = hundreds % 100
num_dozens = int((dozens - (dozens % 10)) / 10) #I'm taking the tens
num_one = dozens % 10 #I'm taking the units
num_multipliction = num_thousands * num_hundreds * num_dozens * num_one

print("Multiplication of the digits of a number " + str(thousands) + " is " + str(num_multipliction))