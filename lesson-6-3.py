# УРОК 6. ЗАДАНИЕ 3

"""
Реализовать базовый класс Worker (работник).
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
● проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


def to_float(str_num: str):
    """to_float() - преобразует строковое значение в числовое с плавающей точкой"""
    try:
        return float(str_num)
    except ValueError:
        return 0


class Worker:

    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        self.name = name.strip()
        self.surname = surname.strip()
        self.position = position.strip()
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name.lower().capitalize() + chr(32) + self.surname.lower().capitalize()

    def get_total_income(self):
        return sum(self._income.values())


print("Введите данные РАБОТНИКА 1 и его должности:")
emp1 = Position(input("ИМЯ       : "), input("ФАМИЛИЯ   : "), input("ДОЛЖНОСТЬ : "),
                to_float(input("ЗАРПЛАТА  : ")), to_float(input("ПРЕМИЯ    : ")))
print("\nВведите данные РАБОТНИКА 2 и его должности:")
emp2 = Position(input("ИМЯ       : "), input("ФАМИЛИЯ   : "), input("ДОЛЖНОСТЬ : "),
                to_float(input("ЗАРПЛАТА  : ")), to_float(input("ПРЕМИЯ    : ")))

print("\nРаботник:", emp1.get_full_name().upper(), "-- Зарплата:", emp1.get_total_income())
print("Работник:", emp2.get_full_name().upper(), "-- Зарплата:", emp2.get_total_income())
