# УРОК 2. ЗАДАНИЕ 3

"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и dict.
"""

seasons_dict = {'зима': {12: "декабрь", 1: "январь", 2: "февраль"},
                'весна': {3: "март", 4: "апрель", 5: "май"},
                'лето': {6: "июнь", 7: "июль", 8: "август"},
                'осень': {9: "сентябрь", 10: "октябрь", 11: "ноябрь"}
                }

m = input("Введите номер месяца: ")
if not m.isdigit() or int(m) > 12:
    print("ОШИБКА! Введите корректный номер месяца!")
else:
    mm = int(m)

    # ВАРИАНТ DICTIONARY
    answer = {mm: [seasons_dict[season].get(mm), season] for season in seasons_dict.keys() if
              mm in seasons_dict[season]}
    print("\nВАРИАНТ DICTIONARY:")
    print(f"Сезон '{answer[mm][-1].upper()}' - Месяц '{answer[mm][0].upper()}'") if len(answer) else print("СЛОВАРЬ "
                                                                                                           "НЕ ЗАДАН!")

    # ВАРИАНТ LIST
    # Предположение: задана только структура данных LIST
    season_list = list(seasons_dict.items())
    # Не рассматриваем вариант преобразования из списка в словарь через ZIP

    print("\nВАРИАНТ LIST:")
    for season, mmm in season_list:
        if mm in mmm.keys():
            print(f"Сезон '{season.upper()}' - Месяц '{mmm.get(mm).upper()}'")
            break
    else:
        print("СЛОВАРЬ НЕ ЗАДАН!")
