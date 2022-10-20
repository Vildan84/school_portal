import csv
from datetime import date


def add_work():
    dic = {"1": "Математика", "2": "Информатика", "3": "Физика", "4": "Геометрия"}
    print()
    print(dic)
    number = input("Выберете предмет: ")
    if number in ["1", "2", "3", "4"]:
        hw = input("Напишите домашнее задание: ")
        day = date.today()
        with open("add_homework.csv", "a", newline='') as file:
            fields = ["Дата", "Математика", "Информатика", "Физика", "Геометрия"]
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writerow({"Дата": day, dic[number]: hw})
    else:
        print("Неверный ввод!!!")
        add_work()
