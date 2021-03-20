# УРОК 5. ЗАДАНИЕ 7

"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры
"""

import json


def to_float(str_num: str):
    """to_float() - преобразует строковое значение в числовое с плавающей точкой"""
    try:
        return float(str_num)
    except ValueError:
        return 0


try:
    with open("text_7.txt", "r", encoding="utf-8") as f_read:  # ФАЙЛ "text_7.txt" предоставлен преподавателем
        with open("l57.json", "w", encoding="utf-8") as f_json:
            prf = {firm.split()[0]: int(to_float(firm.split()[2]) - to_float(firm.split()[3])) for firm in f_read}
            prf_pos_list = [el for el in prf.values() if el > 0]
            average_prf = round(sum(prf_pos_list) / len(prf_pos_list))
            res_list = [prf, {"average_profit": average_prf}]
            print(res_list)
            json.dump(res_list, f_json, ensure_ascii=False, indent=4)
except IOError:
    print("Ошибка ввода-вывода!")
