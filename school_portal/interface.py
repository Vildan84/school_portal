from student import student_menu
from teacher import teacher_menu


def menu():
    while True:
        print()
        print("/////Главное меню/////")
        print("1 - Студент")
        print("2 - Преподаватель")
        print("3 - Выход")
        number = input("Выберете пункт меню: ")

        if number == "1":
            student_menu()
        elif number == "2":
            teacher_menu()
        elif number == "3":
            print()
            print("До свидания!!!")
            break
        else:
            print("Неверный ввод, повторите попытку")