# УРОК 6. ЗАДАНИЕ 4

"""
Реализовать класс Stationery (канцелярская принадлежность).
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return print(f"{self.title}. Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        return print(f"{self.title}. Запуск отрисовки РУЧКОЙ")


class Pencil(Stationery):

    def draw(self):
        return print(f"{self.title}. Запуск отрисовки КАРАНДАШОМ")


class Handle(Stationery):

    def draw(self):
        return print(f"{self.title}. Запуск отрисовки МАРКЕРОМ")


thing = Stationery('Предмет для рисования')
thing.draw()
pen = Pen('Ручка')
pen.draw()
pencil = Pencil('Карандаш')
pencil.draw()
handle = Handle('Маркер')
handle.draw()