# УРОК 5. ЗАДАНИЕ 2

"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке
"""

# СЛОВАМИ СЧИТАЕМ ЛЮБОЕ СОЧЕТАНИЕ СИМВОЛОВ, НЕ ЯВЛЯЮЩИХСЯ символами из списка WHITESPACE и знакамим пунктуации


from string import punctuation


def rm_punctuation(my_str: str):
    for el in punctuation:
        my_str = my_str.replace(el, chr(32))
    return my_str


try:
    words_num = 0
    with open("les52.txt", "r", encoding="utf-8") as f_obj:
        content = f_obj.readlines()
        str_num = len(content)
        for line in content:
            words_num += len(rm_punctuation(line).split())
    print(content)
    print(f"\nКОЛИЧЕСТВО СТРОК : {str_num:>3}\nКОЛИЧЕСТВО СЛОВ  :  {words_num:>3}")
except IOError:
    print("Ошибка ввода-вывода!")
