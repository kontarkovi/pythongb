# УРОК 8. ЗАДАНИЕ 2

"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

"""
from random import random
from re import fullmatch


class MyOperationErr(Exception):
    def __init__(self, err_msg):
        self.err_msg = err_msg


try:
    print('ДЕЛЕНИЕ ЧИСЕЛ. Делимое - случайное число от 0 до 100')
    a = random() * 100
    print(f'ДЕЛИМОЕ   : {a:5.3}')
    match = fullmatch('^\s*[-+]?\d*[.]?\d+(?:[eE][-+]?\d+)?\s*$', input('ДЕЛИТЕЛЬ  : '))
    if match:
        b = float(match[0])
        if b != 0:
            print(f'РЕЗУЛЬТАТ : {a:5.3} / {b:.3} = {a / b: 5.3}')
        else:
            raise MyOperationErr('Деление на ноль!')
    else:
        raise MyOperationErr('Делитель не является числом!')
except MyOperationErr as err:
    print(err)
