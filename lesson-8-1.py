# УРОК 8. ЗАДАНИЕ 1

"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.

Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.

"""
from re import fullmatch
from datetime import date


class MyDateErr(Exception):
    def __init__(self, err_msg):
        self.err_msg = err_msg


class MyDate:
    def __init__(self, str_date: str):
        try:
            self.__raw_str_date = str_date  # Данный атрибут вводится только в целях демонстрации работы методов
            self.yyyy, self.mm, self.dd = MyDate.to_digits(str_date) if str_date else (0, 0, 0)
        except TypeError as err:
            print(err)

    @property
    # Строка, принятая при инициализации объекта
    def raw_str_date(self):
        return self.__raw_str_date

    @property
    # Реальная дата в формате RU, которую содержит объект
    def actual_date(self):
        return chr(45).join(MyDate.valid_date(self.yyyy, self.mm, self.dd).split(chr(45))[::-1])

    @classmethod
    def to_digits(cls, str_date):
        try:
            match = fullmatch(r'\d\d-\d\d-\d{4}', str_date)
            if not match:
                raise MyDateErr(str_date + ' : Некорректный формат даты (ДД-ММ-ГГГГ) или значение')
            dd = int(match[0].split(chr(45))[0])
            mm = int(match[0].split(chr(45))[1])
            yyyy = int(match[0].split(chr(45))[2])
            return yyyy, mm, dd
        except MyDateErr as err:
            print(err)

    @staticmethod
    def valid_date(yyyy, mm, dd):
        try:
            return str(date(yyyy, mm, dd))
        except ValueError as err:
            print(err)
            return ''


md = MyDate('')
print('Инициализированная строка:', md.raw_str_date)
# Валидация года
print('Принятая дата:', md.valid_date(md.yyyy, md.mm, md.dd), '\n')
# Валидация месяца
md = MyDate('30-13-1970')
print('Инициализированная строка:', md.raw_str_date)
print('Принятая дата:', md.valid_date(md.yyyy, md.mm, md.dd), '\n')
# Валидация дня
md = MyDate('29-02-2019')
print('Инициализированная строка:', md.raw_str_date)
print('Принятая дата:', md.valid_date(md.yyyy, md.mm, md.dd), '\n')

# Исправляем актуальную дату
md.yyyy, md.mm, md.dd = MyDate.to_digits('28-02-2019')
print('Инициализированная строка:', md.raw_str_date)
print('Принятая дата:', MyDate.valid_date(md.yyyy, md.mm, md.dd))
print('Актуальная дата, RU:', md.actual_date, '\n')

md.yyyy, md.mm, md.dd = MyDate.to_digits('28-02-0345')
print('Принятая дата:', MyDate.valid_date(md.yyyy, md.mm, md.dd))
print('Актуальная дата, RU:', md.actual_date, '\n')
