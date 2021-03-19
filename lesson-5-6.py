# УРОК 5. ЗАДАНИЕ 6

"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

from string import punctuation


def to_float(str_num: str):
    """to_float() - преобразует строковое значение в числовое с плавающей точкой"""
    try:
        return float(str_num)
    except ValueError:
        return 0


def rm_punctuation(my_str: str):
    """rm_punctuation() - заменяет в строке все знаки пунктуации за исключением точки на пробел"""
    new_str = "".join([chr(32) if ord(smb) != 46 and smb in punctuation else smb for smb in my_str])
    return new_str


def get_dig_list(my_list):
    """get_dig_list() - преобразует список в список c только числовыми значениями"""
    return [to_float(el) for el in my_list]


try:
    with open("text_6.txt", "r", encoding="utf-8") as f_obj:
        content = f_obj.readlines()
        subj_dict = {subj[:subj.find(':')]: int(sum(get_dig_list(rm_punctuation(subj).split())))for subj in content}
        print(subj_dict)
except IOError:
    print("Ошибка ввода-вывода!")
