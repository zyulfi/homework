# Задача 4
# Потребител въвежда аритметичен израз от клавиатурата. Например, 23+12.
# # Резултатът от израза трябва да се изведе на екрана. В нашия пример той е 35.
# Един аритметичен израз може да се състои само от три части: число, операция, число.
# Възможните операции са +, -, *, /.

aritm_express = input("Please arithmetic expression: ")
left_num = ""
flag_left = True
right_num = ""
aritm_operation = ""

for i in aritm_express:
    if (48 <= ord(i) <= 57) and (ord(i) != 43 or ord(i) != 45 or ord(i) != 42 or ord(i) != 47)\
            and flag_left == True:
        left_num += i

    elif ord(i) == 43 or ord(i) == 45 or ord(i) == 42 or ord(i) == 47:
        flag_left = False
        aritm_operation = i

    elif (48 <= ord(i) <= 57) and (ord(i) != 43 or ord(i) != 45 or ord(i) != 42 or ord(i) != 47)\
            and flag_left == False:
        right_num += i

if left_num.isdigit() and right_num.isdigit():
    if ord(aritm_operation) == 43:
        sum_num = int(left_num) + int(right_num)
        print(f"The sum of the numbers is {sum_num}")
    elif ord(aritm_operation) == 45:
        diff_num = int(left_num) - int(right_num)
        print(f"The difference of the numbers is: {diff_num}")
    elif ord(aritm_operation) == 42:
        multipl_num = int(left_num) * int(right_num)
        print(f"The multiplication of numbers is: {multipl_num}")
    elif ord(aritm_operation) == 47:
        if int(right_num) == 0:
            print("Is not divisible by 0")
        else:
            div_num = int(left_num) / int(right_num)
            print(f"The quotient of the numbers is: {div_num}")
else:
    print("Аrithmetic expression cannot contain letters")



