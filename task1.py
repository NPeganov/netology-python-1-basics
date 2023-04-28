"""
Задание 1
Даны 2 переменных, в которых хранятся строки произвольной длины: phrase_1 и phrase_2.
Напишите код, который проверяет какая из этих строк длиннее.

Примеры работы программы:

phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

Результат:
Фраза 1 длиннее фразы 2 2.

phrase_1 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
phrase_2 = 'Насколько проще было бы писать программы, если бы не заказчики'
Результат:
Фраза 2 длиннее фразы 1 3.

phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = 'Насколько проще было бы писать программы, если бы не заказчики'
Результат:
Фразы равной длины

"""


def comparison(phrase_1, phrase_2):
    phrase_1 = len(phrase_1)
    phrase_2 = len(phrase_2)
    result = 'equal to'
    if phrase_1 > phrase_2:
        result = 'longer than'
    elif phrase_1 < phrase_2:
        result = 'shorter than'

    return result


if __name__ == '__main__':
    phrase_1 = input("Enter phrase_1: ")
    phrase_2 = input("Enter phrase_2: ")
    result = comparison(phrase_1, phrase_2)
    print(f"Phrase 1 is {result} phrase 2")
