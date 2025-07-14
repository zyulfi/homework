# Да се създаде програма, която проверява входните данни.

name = input("Моля, въведете потребителско име: ")
password = input("Моля, въведете парола: ")

while True:
    name_user = input("Моля, въведете потребителско име: ")
    pass_user = input("Моля, въведете парола: ")
    if name_user != name:
        while name_user != name:
            name_user = input("Грешно потребителско име: ")
        if pass_user == password:
            print("Добре дошъл, " + name)
            break
        else:
            while pass_user != password:
                pass_user = input("Грешна парола: ")
            print("Добре дошъл, " + name)
            break
    else:
        if pass_user == password:
            print("Добре дошъл, " + name)
            break
        else:
            while pass_user != password:
                pass_user = input("Грешна парола: ")
            print("Добре дошъл, " + name)
            break