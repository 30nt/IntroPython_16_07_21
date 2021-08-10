# модули в пайтон
# функции

from random import randint
# from string import ascii_lowercase as alphabet
# import numpy as np  -- общепринятое сокращение
# import pandas as pd
# print(alphabet)

# triangle = [[1, 3], [2, -5], [-3, 0]]
# triangle_1 = ([1, 3], [2, -5], [-3, 0])
# triangle_1[0][0] = 10
# print(triangle_1)

def create_triangle():
    triangle = {"A": {"x": randint(-10, 10), "y": randint(-10, 10)},
                "B": {"x": randint(-10, 10), "y": randint(-10, 10)},
                "C": {"x": randint(-10, 10), "y": randint(-10, 10)}}
    return triangle


def print_list(some_list):
    for line in some_list:
        print(line)


triangle_2 = create_triangle()
triangle_3 = create_triangle()
triangle_4 = create_triangle()

triangle_list = [triangle_2, triangle_3, triangle_4]
print_list(triangle_list)
print_list([1,2,3,4,5])