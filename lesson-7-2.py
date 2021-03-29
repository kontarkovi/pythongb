# УРОК 7. ЗАДАНИЕ 2

"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.

Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod

cloth_consumption = [0]


class ClothABC(ABC):

    @abstractmethod
    def consumption(self):
        pass


class Cloth(ClothABC):
    __total_cloth_consumption = [0]

    def __init__(self, name, new_consumption):
        self.__total_cloth_consumption[0] += new_consumption
        self.name = name

    def __del__(self):
        self.__total_cloth_consumption[0] -= self.consumption
        print(f"ИСКЛЮЧЕНО : {self.name}")

    @property
    def consumption(self):
        return self.__total_cloth_consumption[0]

    @property
    def all_cloth_type_consumption(self):
        return self.__total_cloth_consumption[0]


class Coat(Cloth):

    def __init__(self, name, sz_vol: int):
        super().__init__(name, sz_vol / 6.5 + 0.5)
        self.__sz_vol = sz_vol

    @property
    def consumption(self):
        return self.__sz_vol / 6.5 + 0.5

    @property
    def cloth_sz(self):
        return self.__sz_vol


class Suit(Cloth):

    def __init__(self, name, sz_h: float):
        super().__init__(name, 2 * sz_h + 0.3)
        self.__sz_h = sz_h

    @property
    def consumption(self):
        return 2 * self.__sz_h + 0.3

    @property
    def cloth_sz(self):
        return self.__sz_h


coat1 = Coat('Пальто зимнее', 48)
print(f"{coat1.name:20}, размер : {coat1.cloth_sz:5}, требуется ткани : {coat1.consumption:.3}")

suit1 = Suit('Костюм женский', 1.8)
print(f"{suit1.name:20}, рост   : {suit1.cloth_sz:5}, требуется ткани : {suit1.consumption:.3}")

coat2 = Coat('Пальто осеннее', 52)
print(f"{coat2.name:20}, размер : {coat2.cloth_sz:5}, требуется ткани : {coat2.consumption:.3}")

print(f"СУММАРНЫЙ РАСХОД ТКАНИ : {coat1.all_cloth_type_consumption:.4}")

del coat2

print(f"СУММАРНЫЙ РАСХОД ТКАНИ : {coat1.all_cloth_type_consumption:.4}")
