# УРОК 3. ЗАДАНИЕ 3

"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
"""
from typing import List, Any


def my_func(x, y, z):
    func_list = list((x, y, z))
    func_list.sort(reverse=True)
    return func_list[0] + func_list[1]


try:
    print("ВВЕДИТЕ ТРИ ЧИСЛА:")
    my_list = [float(input(f"{i+1} : ")) for i in range(0,3) ]
    print(f"Сумма наибольших двух = {my_func(my_list[0], my_list[1], my_list[2])}")
except ValueError:
    print("ОШИБКА! Вводите числа!")