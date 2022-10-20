from viewer import view_homework as vh
from viewer import view_schedule as vs
from viewer import view_courses as vc
from enroll import enroll_to_courses as atc


def student_menu():
    print()
    print("1. Посмотреть расписание на сегодня")
    print("2. Посмотреть домашнее задание")
    print("3. Посмотреть доп. курсы")
    print("4. Записаться на курсы")
    print("Для выхода в главное меню введите символ не из списка")

    num = input("Выберете пункт меню: ")
    if num == "1":
        print()
        print(vs())
    elif num == "2":
        print()
        print(vh())
    elif num == "3":
        print()
        print(vc())
    elif num == "4":
        atc()