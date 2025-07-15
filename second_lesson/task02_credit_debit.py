#Задача 2
#Потребител въвежда три числа от клавиатурата.
# Първото число е месечната заплата, второто е сумата на месечния банков кредит,
# а третото е сметката за комунални услуги.
# Трябва да се изведе сумата, която остава на потребителя след всички плащания.

num_salary = float(input("Please enter your salary: "))
num_credit = float(input("Please enter the amount of the monthly bank loan: "))
num_utilities = float(input("Please enter the utility bill: "))

num_lack = num_salary - (num_credit + num_utilities)
print(num_lack)

#In addition to what we learned about conditional constructions
if num_lack < 0:
    print("You are overspending with: " + str(abs(num_lack)) + "лв.")
elif num_lack == 0:
    print("Your salary is enough to cover your expenses.")
else:
    print("You are in excess of " + str(num_lack) + "лв and you have the opportunity to save money on travel.")