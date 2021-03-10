# УРОК 3. ЗАДАНИЕ 1
"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль
"""


def divide2dig(x, y):
    'divide2dig() - возвращает результат деления двух чисел'
    try:
        return x / y
    except ZeroDivisionError:
        print("ОШИБКА! Деление на ноль!")
    except ValueError:
        print("ОШИБКА! Не является числом!")
    except TypeError:
        print("ОШИБКА! Не является числом!")


digits = []
try:
    for _ in (digits.append(float(input(f'Введите число {"X" if ind == 0 else "Y"} : '))) for ind in range(0, 2)):
        pass
    print(digits)
    x, y = digits[0], digits[1]
    print(f"ДЕЛЕНИЕ: {x} / {y} = {divide2dig(x, y)}")
    print('--',divide2dig.__doc__)
except ValueError:
        print("ОШИБКА! Не является числом!")
