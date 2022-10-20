from viewer import view_homework as vh
from viewer import view_schedule as vs
from add_homework import add_work as aw
from option import add_option
from export import create_txt


def teacher_menu():
    print()
    print("1. Посмотреть расписание")
    print("2. Посмотреть домашнее задание")
    print("3. Добавить домашнее задание")
    print("4. Добавить курсы")
    print("5. Экспортировать запись на курсы")
    print("Для выхода в главное меню введите символ не из списка")
    num = input("Выберете пункт меню: ")

    if num == "1":
        print()
        print(vs())
    if num == "2":
        print()
        print(vh())
    if num == "3":
        aw()
    if num == "4":
        add_option()
    if num == "5":
        create_txt()
