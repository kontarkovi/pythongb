# УРОК 8. ЗАДАНИЕ 7

"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

"""

from random import randint


class ComplexNumber:

    def __init__(self, re_z, im_z):
        self.re_z = re_z
        self.im_z = im_z

    def __add__(self, other):
        return ComplexNumber(self.re_z + other.re_z, self.im_z + other.im_z)

    def __mul__(self, other):
        return ComplexNumber(self.re_z * other.re_z - self.im_z * other.im_z,
                             self.re_z * other.im_z + self.im_z * other.re_z)

    def __str__(self):
        sign = ''
        if self.im_z >= 0:
            sign = '+'
        return '(' + str(self.re_z) + sign + str(self.im_z) + 'j)'


cn1 = ComplexNumber(randint(-100, 100), randint(-100, 100))
print('Мнимое число 1:', cn1)
cn2 = ComplexNumber(randint(-100, 100), randint(-100, 100))
print('Мнимое число 2:', cn2)
print('Сумма чисел 1 и 2:', cn1 + cn2)
print('Произведение чисел 1 и 2:', cn1 * cn2)
cn3 = ComplexNumber(randint(-100, 100), 0)
print('Мнимое число 3:', cn3)
