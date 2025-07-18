#Задача 8
#Потребител въвежда четирицифрено число от клавиатурата.
#Числото трябва да бъде превърнато и резултатът да бъде изведен.
#Например, ако въведете 4512, резултатът е 2154.

thousands = input("Please enter a four-digit number: ")

while True:
    if thousands.isdigit() and len(thousands) == 4:
        int_thousands = int(thousands)
        num_thousands = int((int_thousands - (int_thousands % 1000)) / 1000) #I take the thousandths
        hundreds = int_thousands % 1000
        num_hundreds = int((hundreds - (hundreds % 100)) / 100) #I take the hundreds
        dozens = hundreds % 100
        num_dozens = int((dozens - (dozens % 10)) / 10) #I take the hundreds
        num_one = dozens % 10 #I take the units
        break
    else:
        print('You must enter a four-digit number')
        thousands = input('Еnter a four-digit number:')

print(str(num_one) + str(num_dozens) + str(num_hundreds) + str(num_thousands))
