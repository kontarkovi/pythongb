# УРОК 6. ЗАДАНИЕ 1

"""
Создать класс TrafficLight (светофор).

● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

from time import sleep


class TrafficLight:

    def __init__(self, color: str):
        self.__color = color.upper()

    def running(self, color: str):
        print(f"Current light is {self.__color}. ", end="")
        if self.__color == 'RED' and color.upper() == 'YELLOW':
            wait_sec = 7
            next_light = "GREEN"
        elif self.__color == 'YELLOW' and color.upper() == 'GREEN':
            wait_sec = 2
            next_light = "RED"
        elif self.__color == 'GREEN' and color.upper() == 'RED':
            wait_sec = 10
            next_light = "YELLOW"
        else:
            print("The light order has been broken!")
            return ""
        print(f"The next light is {color.upper()}")
        print(f"Wait {wait_sec} sec ...\n")
        sleep(wait_sec)
        self.__color = color.upper()
        return next_light


iterations = 5
tl = TrafficLight('yellow')
to_switch_on = "green"
# to_switch_on = "red"
for i in range(1, iterations+1):
    to_switch_on = tl.running(to_switch_on)
    if not bool(to_switch_on):
        break
