# УРОК 5. ЗАДАНИЯ 4 и 5

"""
4. Создать (не программно) текстовый файл со следующим содержимым:

One — 1

Two — 2

Three — 3

Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

# Создаём англо-русский словарь. При желании можно использовать функцию онлайн-перевода для получения перевода слова
en_ru_dict = {'One': ['Один', 1], 'Two': ['Два', 2], 'Three': ['Три', 3], 'Four': ['Четыре', 4]}


def num_replace(my_str: str, my_dict: dict):
    for num in my_dict:
        num_count = my_str.count(num)
        my_str = my_str.replace(num, my_dict.get(num)[0], num_count)
    return my_str


def to_float(str_num: str):
    try:
        return float(str_num)
    except ValueError:
        return 0


try:
    with open("text_4.txt", "r", encoding="utf-8") as f_read:  # ФАЙЛ "text_4.txt" предоставлен преподавателем
        eof = False
        with open("les54.txt", "a", encoding="utf-8") as f_write:
            while not eof:
                f_str = f_read.readline()
                f_write.write(num_replace(f_str, en_ru_dict))
                eof = not bool(f_str)

    # В задании 5 указано создать набор чисел, разделенных пробелами
    # Воспользуемся только что созданным файлом. Но вместо пробелов используем разделитель chr(45)
    with open("les54.txt", "r", encoding="utf-8") as f_read:
        content = f_read.readlines()
        num_list = [to_float(el.strip().split(chr(45))[1]) for el in content]
        print(f"Сумма чисел в файле: {sum(num_list)}")
except IOError:
    print("Ошибка ввода-вывода")
