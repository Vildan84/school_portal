import csv


def create_txt(name="new_export"):
    print()
    dic = {"1": "Математика", "2": "Информатика", "3": "Физика", "4": "Геометрия"}
    print(dic)
    number = input("Выберете предмет: ")
    if number in ["1", "2", "3", "4"]:
        name = input("Введите имя файла: ")
        page = open(f"files/{name}.txt", 'w')
        with open("enroll_in_courses.csv", "r", newline='') as csvfile:
            txt = ""
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row[dic[number]] != "":
                    txt += f'{row[dic[number]]}\n'
            page.write(txt)
    else:
        print("Неверный ввод!!!")
        create_txt()