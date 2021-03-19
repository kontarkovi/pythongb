# УРОК 5. ЗАДАНИЕ 1

"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка
"""

try:
    end_of_inp = False
    print("ВВОД ДАННЫХ ДЛЯ ЗАПИСИ В ФАЙЛ")
    with open("l51.txt", "w", encoding="utf-8") as f_obj:
        while not end_of_inp:
            f_obj.write(str_inp := input("Введите строку [<''> - Завершить]: "))
            f_obj.write("\n") if str_inp != "" else print("Ввод завершён!")
            end_of_inp = not bool(str_inp)
except IOError:
    print("Ошибка ввода-вывода!")