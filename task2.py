"""
Задание 2
Дана переменная, в которой хранится число (год). Необходимо написать программу, которая выведет, является ли
данный год високосным или обычным.

Пример работы программы:

year = 2020
Результат:
Високосный год

year = 2019
Результат:
Обычный год

"""


from common.digital_input import digital_input


if __name__ == '__main__':
    year = digital_input('Enter the year: ')
    if year % 4 == 0 and year % 100 != 0:
        print("The year is leap")
    else:
        print("The year is not leap")
