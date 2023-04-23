"""
Дана переменная, в которой хранится шестизначное число (номер проездного билета). Напишите программу, которая будет определять, является ли данный билет "счастливым". Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера.

Примеры работы программы:

number = 123456
Результат:
Несчастливый билет

number = 123321
Результат:
Счастливый билет

"""


from common.digital_input import digital_input


def ticket(number):
    a1 = number // 100000
    a2 = number // 10000 % 10
    a3 = number // 1000 % 10
    a4 = number // 100 % 10
    a5 = number // 10 % 10
    a6 = number % 10
    if a1 + a2 + a3 == a4 + a5 + a6:
        print("A lucky ticket!😀")
    else:
        print("Not a lucky ticket 😔")


if __name__ == '__main__':
    number = digital_input('Enter the number: ')
    ticket(number)
