import numpy as np


def triangle_square(a, b, c):
    p = (a + b + c) / 2
    return np.sqrt(p * (p - a) * (p - b) * (p - c))
