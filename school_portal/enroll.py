import csv


def enroll_to_courses():
    print()
    dic = {"1": "Математика", "2": "Информатика", "3": "Физика", "4": "Геометрия"}
    print(dic)
    number = input("Выберете предмет доп курса: ")
    if number in ["1", "2", "3", "4"]:
        name = input("Введите имя и фамилию: ")
        with open("enroll_in_courses.csv", "a", newline='') as file:
            fields = ["Математика", "Информатика", "Физика", "Геометрия"]
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writerow({dic[number]: name})
    else:
        print("Неверный ввод")
        enroll_to_courses()
