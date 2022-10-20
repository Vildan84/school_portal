import csv


def view_homework():
    dic = {"1": "Математика", "2": "Информатика", "3": "Физика", "4": "Геометрия"}
    print()
    print(dic)
    print("Нажми другие цифры чтоб вывести все предметы")
    print()
    number = input("Выберете предмет: ")
    if number in ["1", "2", "3", "4"]:
        print(f"/////Домашнее задание {dic[number]}/////")
        with open("add_homework.csv", 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row[dic[number]] != "":
                    print(row["Дата"], row[dic[number]])
    else:
        with open("add_homework.csv", 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)


def view_schedule():
    print("/////РАСПИСАНИЕ/////")
    with open("schedule.txt", 'r') as file:
        sc = file.read()
        return sc


def view_courses():
    print("/////Курсы/////")
    with open("courses.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(", ".join(row[None]))
