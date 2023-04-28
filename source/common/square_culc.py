import numpy as np


def circle_square(r):
    return np.pi * r ** 2


def rectangle_square(a, b):
    return a * b


def triangle_square(a, b, c):
    p = (a + b + c) / 2
    return np.sqrt(p * (p - a) * (p - b) * (p - c))
