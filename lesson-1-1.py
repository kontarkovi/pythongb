# УРОК 1. ЗАДАНИЕ 1
"""
Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
несколько чисел и строк и сохраните в переменные, выведите на экран
"""
num_int = 123  # Переменная целочисленного типа
num_float = 456.78  # Переменная числа с плавающей точкой
num_sum = num_int + num_float  # Переменная суммы чисел разных типов
str1 = '-'*len(str(num_sum))
str2 = 'Simple String Text'

print(f"\nПеременная 1: {num_int} - {type(num_int)}\nПеременная 2: {num_float} - {type(num_float)}\n{str1:>20}")
print('СУММА: {:>13.2f}'.format(num_sum))
print(f'\nЭто простая строка: "{str2}" - {type(str2)}\n')

a = input("Введите строку символов 1: ")
b = input("Введите строку символов 2: ")
c = input("Введите целое число: ")
d = input("Введите вещественное число: \n")

print("1:'" + a + "'")
print("2:'" + b + "'")
print(f"1: {int(float(c))}")
print(f"2: {float(d)}")
