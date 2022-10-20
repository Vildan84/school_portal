import csv


def add_option():
    print()
    print("Добавьте дополнительные курсы ")
    date = input("Введите дату курса: ")
    subject = input("Введите предмет: ")
    courses = input("Введите описание: ")
    with open("courses.csv", "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([date, subject, courses])

