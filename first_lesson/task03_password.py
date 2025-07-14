# Да се създаде програма, която проверява входните данни.

name = input("Please enter username: ")
password = input("Please enter password: ")

while True:
    name_user = input("Please enter username: ")
    pass_user = input("Please enter password: ")
    if name_user != name:
        while name_user != name:
            name_user = input("Wrong username: ")
        if pass_user == password:
            print("Welcome " + name)
            break
        else:
            while pass_user != password:
                pass_user = input("Wrong password: ")
            print("Добре дошъл, " + name)
            break
    else:
        if pass_user == password:
            print("Welcome " + name)
            break
        else:
            while pass_user != password:
                pass_user = input("Wrong password: ")
            print("Welcome " + name)
            break