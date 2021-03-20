# УРОК 5. ЗАДАНИЕ 3

"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников
"""

try:
    with open("text_3.txt", "r", encoding="utf-8") as f_obj:  # ФАЙЛ "text_3.txt" предоставлен преподавателем
        income = 0
        surname_min = []
        content = f_obj.readlines()
        print("СОТРУДНИКИ с ДОХОДОМ МЕНЕЕ 20000:")
        for emp in content:
            emp_income = float(emp.strip().split()[1])
            income += emp_income
            if emp_income < 20000:
                print(f"{emp.strip().split()[0]:15} ---> {emp_income}")
        average_income = 0
        print(f"\nСРЕДНИЙ ДОХОД ВСЕХ СОТРУДНИКОВ: {income / len(content)}")
except IOError:
    print("Ошибка ввода-вывода!")
