"""
Задание 4
Вам нужно написать программу для подбора упаковок по размерам товара. Размеры (ширина, длина, высота) хранятся в
переменных (в сантиметрах):

Используйте следующие правила:

если каждое из трех измерений менее или равно 15 сантиметрам, то выведите на экран "Коробка №1";
если хотя бы одно из измерений больше 2 метров, то выводите "Упаковка для лыж";
если хотя бы одно из измерений больше 15 сантиметров, но менее 50 сантиметров, то выводите "Коробка №2";
во всех остальных случаях выводите "Коробка №3".
Пример работы программы:

width = 15
length = 55
height = 15
Результат:
Стандартная коробка №3

width = 45
length = 205
height = 45
Результат:
Ищите упаковку для лыж

"""


from common.digital_input import digital_input


if __name__ == '__main__':
    width = digital_input('Enter the width (sm): ')
    length = digital_input('Enter the length (sm): ')
    height = digital_input('Enter the height (sm): ')
    if (width <= 15) and (length <= 15) and (height <= 15):
        box = 'box 1'
    elif (width > 200) or (length > 200) or (height > 200):
        box = 'ski packaging'
    elif (15 < width < 50) or (15 < length < 50) or (15 < height < 50):
        box = 'box 2'
    else:
        box = 'box 3'

    print(box)
