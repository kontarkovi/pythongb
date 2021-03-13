# УРОК 3. ЗАДАНИЕ 5

"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def to_float(str_num: str):
    try:
        return float(str_num)
    except ValueError:
        return 0


def sum_numbers_with_exit(user_str: str, exit_ind):
    str_list = user_str.split(chr(32))
    dig_sum = 0
    stop_inp = False
    for el in str_list:
        dig_sum += to_float(el)
        for ex in exit_ind:
            ex_ind = el.find(ex)
            if ex_ind == -1:
                continue
            else:
                dig_sum += to_float(el[0:ex_ind])
                stop_inp = True
                break
        if stop_inp:
            break
    return dig_sum, stop_inp


print("Введите числа, разделённые пробелом [Enter - Продолжить] [Q - Выход] :")
isExit = False
exit_enum = chr(81), chr(113), chr(1081), chr(1049)
num_sum = 0
while not isExit:
    str_numbers = input()
    cur_sum, isExit = sum_numbers_with_exit(str_numbers, exit_enum)
    num_sum += cur_sum
    print(f"Сумма вновь введённых чисел = {cur_sum}")
    print(f"Итоговая сумма = {num_sum}")
    if not isExit:
        print("Продолжите ввод [Enter - Продолжить] [Q - Выход] :")