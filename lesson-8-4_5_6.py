# УРОК 8. ЗАДАНИЯ: 4, 5, 6

"""
4.
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

5.
Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

"""

from abc import ABC, abstractmethod
from pandas import DataFrame
from tabulate import tabulate
from re import fullmatch
from datetime import date


class MyOperationErr(Exception):
    def __init__(self, err_msg):
        self.err_msg = err_msg


class WareHouse(ABC):

    @abstractmethod
    def sign_for(self, *args):
        pass

    @abstractmethod
    def issue(self, *args):
        pass


class OfficeEquipment:

    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def __str__(self):
        return self.brand.upper() + ' ' + self.model


class Printer(OfficeEquipment):
    def __init__(self, *args):
        brand, model, self.prn_type, self.color = args
        super().__init__(brand, model)


class Scanner(OfficeEquipment):
    def __init__(self, *args):
        brand, model, self.scn_format, self.dpi = args
        super().__init__(brand, model)


class Xerox(OfficeEquipment):
    def __init__(self, *args):
        brand, model, self.speed = args
        super().__init__(brand, model)


class OEQWareHouse(WareHouse):

    def __init__(self):
        self.inventories = dict()

    def sign_for(self, *args):
        equipment, amount, contractor = args
        if self.inventories.get(str(equipment)):
            self.inventories[str(equipment)].append([date.today(), 'поступление', amount, contractor])
        else:
            new_el = {str(equipment): [[date.today(), 'поступление', amount, contractor]]}
            self.inventories = {**self.inventories, **new_el}

    def issue(self, equipment, amount, recipient):
        # проверить есть ли в наличии на складе
        val = self.remains(str(equipment))
        if amount <= val > 0:
            self.inventories[str(equipment)].append([date.today(), 'выдача', amount, recipient])
            print(equipment, f'запрос {amount} ед.', 'выдано в', recipient, amount, 'ед.')
        elif 0 < val < amount:
            print(equipment, f'запрос {amount} ед.', ': недостаточно на складе')
        else:
            print(equipment, f'запрос {amount} ед.', ': нет на складе')

    def remains(self, equipment):
        val = 0
        records = self.inventories.get(str(equipment))
        if records:
            for rec in records:
                if rec[1] == 'поступление':
                    val += rec[2]
                elif rec[1] == 'выдача':
                    val -= rec[2]
        return val

    def report(self):
        print('\nТЕКУЩЕЕ СОСТОЯНИЕ СКЛАДА:')
        if not self.inventories.keys():
            print('( -- НЕТ ТМЦ -- )')
        for inv in self.inventories.keys():
            print('\n', inv, f'(Остаток : {self.remains(inv)} ед.)')
            print(tabulate(DataFrame(self.inventories.get(inv)), showindex=False))
            self.inventories.get(inv)

    @staticmethod
    def checkup_input(pattern: str, inp_msg: str, err_msg: str):
        while True:
            try:
                match = fullmatch(pattern, inp_str := input(inp_msg))
                if match:
                    return match[0]
                else:
                    if not inp_str:
                        break
                    else:
                        raise MyOperationErr(err_msg)
            except MyOperationErr as err:
                print(err)


prn1 = Printer('Brother', 'HL-J6000DW', 'струйный', 'цветной')
prn2 = Printer('Canon', 'i-SENSYS LBP112', 'струйный', 'цветной')
prn3 = Printer('HP', 'LaserJet M236sdw', 'лазерный', 'ч/б')
prn4 = Printer('Brother', 'HL-J6000DW', 'струйный', 'цветной')
scn1 = Scanner('Canon', 'CanoScan LiDE 300', 'A4', '2400x2400')
scn2 = Scanner('Epson', 'Perfection V19', 'A4', '4800x4800')
scn3 = Scanner('Fujitsu', 'ScanPartner SP1120', 'A4', '600x600')
cp1 = Xerox('Xerox', 'DocuColor 12', '50')
cp2 = Xerox('KYOCERA', 'TASKalfa 221', '22')

eq_for_invoice = [prn1, prn2, cp2, prn4]
print('ОРГТЕХНИКА ДЛЯ ПОСТУПЛЕНИЯ НА СКЛАД:')
for eq in enumerate(eq_for_invoice, 1):
    print(eq[0], eq[1])

myWH = OEQWareHouse()
# Отчёт по складу
myWH.report()

# Подготовка счёта-фактуры и поступление
print('\nПОДГОТОВКА СЧЁТА-ФАКТУРЫ:')
for eq in eq_for_invoice:
    quantity = OEQWareHouse.checkup_input(r'^\s*\d+\s*$', f'{eq.brand} {eq.model}, КОЛИЧЕСТВО : ', 'Введите число!')
    if not quantity:
        print('Некорректные данные! Невозможно подготовить счёт-фактуру.')
        break
    supplier = OEQWareHouse.checkup_input(r'^[\w\s]+$', f'{eq.brand} {eq.model}, ПОСТАВЩИК  : ',
                                          'Название поставщика: Минимум 5 символов, Максимум 20 символов!')
    if not supplier:
        print('Некорректные данные! Невозможно подготовить счёт-фактуру.')
        break
    # Поступление на склад
    myWH.sign_for(eq, int(quantity), supplier)

# Отчёт по складу
myWH.report()

# Выдача в отделы компании
print('\nВЫДАЧА ТМЦ В ОТДЕЛ:')
myWH.issue(prn1, 10, 'ОК')
myWH.issue(prn2, 1, 'ОТиЗ')
myWH.issue(scn3, 1, 'ОТиЗ')

# Отчёт по складу
myWH.report()
