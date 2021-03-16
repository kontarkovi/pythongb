# УРОК 4. ЗАДАНИЕ 7

"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24
"""
from functools import reduce
from itertools import count


def multiply(prev, cur):
    return prev * cur


def fact(n=0):
    for nn in count(1):
        for elem in [reduce(multiply, range(1, nn + 1))]:
            yield elem
        if nn >= n:
            break


for el in fact(15):
    print(el)
