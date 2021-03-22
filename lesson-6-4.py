# УРОК 6. ЗАДАНИЕ 4

"""
Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.

"""


class Car:

    def __init__(self, speed: float, color: str, name, is_polis=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polis = is_polis

    def go(self):
        return print(f"Машина {self.name} ПОЕХАЛА")

    def stop(self):
        return print(f"Машина {self.name} ОСТАНОВИЛАСЬ")

    def turn(self, direction):
        return print(f"Машина {self.name} ПОВЕРНУЛА {direction}")

    def show_speed(self):
        return print(f"Машина {self.name}. СКОРОСТЬ: {self.speed} км/час")


class TownCar(Car):

    def show_speed(self):
        return print(f"Городское авто {self.name}. СКОРОСТЬ: {self.speed} км/час {'ПРЕВЫШЕНИЕ!' if self.speed > 60 else ''}")


class WorkCar(Car):

    def show_speed(self):
        return print(f"Грузовое авто {self.name}. СКОРОСТЬ: {self.speed} км/час {'ПРЕВЫШЕНИЕ!' if self.speed > 40 else ''}")


class SportCar(Car):
    pass


class PoliceCar(Car):

    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name, True)


car = TownCar(50, 'red', 'Toyota Corolla')
car1 = TownCar(70, 'black', 'Honda Pilot')
police = PoliceCar(100, 'white-blue', 'Ford Focus Police')
truck = WorkCar(50, 'silver', 'IVECO')
sport = SportCar(150, 'green', 'Subaru')

car.go()
car1.go()
police.go()
truck.go()
sport.go()

car.show_speed()
car1.show_speed()
police.show_speed()
truck.show_speed()
sport.show_speed()

car1.stop()
truck.stop()
