# Задача 5
# В списък от цели числа, попълнен със случайни числа, определете минималния и максималния елемент,
# пребройте броя на отрицателните елементи, пребройте броя на положителните елементи и
# пребройте броя на нулите. Изведете резултатите на екрана.

list_num = [-5, -20, 0 , 25 , 50]
max_num = list_num[0]
min_num = list_num[0]
counter_positive_number = 0
counter_negative_number = 0
counter_null = 0

for i in range(len(list_num)):
    if list_num[i] > max_num:
        max_num = list_num[i]
    elif list_num[i] < min_num:
        min_num = list_num[i]

for i in range(len(list_num)):
    if list_num[i] > 0:
        counter_positive_number += 1
    elif list_num[i] < 0:
        counter_negative_number += 1
    else:
        counter_null += 1

print(f"Max number is: {max_num}")
print(f"Min number is: {min_num}")
print(f"Тhe number of negative numbers is: {counter_negative_number}")
print(f"Тhe number of positive numbers is: {counter_positive_number}")
print(f"The number of 0 is: {counter_null}")