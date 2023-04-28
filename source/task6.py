"""
Задание 6 (необязательное)

Напишите программу, которая сможет вычислять площади трех фигур (круг, треугольник и прямоугольник).
Тип фигуры запрашиваем через пользовательский ввод, после чего делаем запрос характеристик фигуры:

если пользователь выбрал круг, запрашиваем его радиус,
если треугольник – длины трех его сторон;
если прямоугольник – длины двух его сторон.
Пример работы программы:

Введите тип фигуры:
Круг

Введите радиус круга:
10
Результат:
Площадь круга: 314.16

Введите тип фигуры:
Треугольник

Введите длину стороны A:
2

Введите длину стороны B:
2

Введите длину стороны C:
3
Результат:
Площадь треугольника: 1.98

"""

from common.digital_input import digital_input
from common.square.circle import circle_square
from common.square.triangle import triangle_square
from common.square.rectangle import rectangle_square


if __name__ == '__main__':
    s = None
    figure_type = None
    while figure_type is None:
        figure_type = input("Enter the type of a figure: ").lower()
        if (figure_type == 'triangle') or (figure_type == 'треугольник'):
            a = digital_input("Enter the first side: ")
            b = digital_input("Enter the second side: ")
            c = digital_input("Enter the third side: ")
            s = triangle_square(a, b, c)
        elif (figure_type == 'circle') or (figure_type == 'круг'):
            r = digital_input("Enter the radius: ")
            s = circle_square(r)
        elif (figure_type == 'square') or (figure_type == 'rectangle') or (figure_type == 'квадрат'):
            a = digital_input("Enter the first side: ")
            b = digital_input("Enter the second side: ")
            s = rectangle_square(a, b)
        else:
            figure_type = None
            print('Wrong type')

    print(f"The square = {s}")
