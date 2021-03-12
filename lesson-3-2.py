# УРОК 3. ЗАДАНИЕ 2
"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой
"""


def printout_udata(name, surname, birth_year, city, email, phone):
    return f"Фамилия: {surname.upper()}, Имя: {name.upper()}, Год рождения: {birth_year:4}, " \
           f"Город проживания: {city.upper()}, email: {email}, телефон: {phone}"


user_desc = ['имя', 'фамилия', 'год рождения', 'город проживания', 'email', 'телефон']
print("ВВЕДИТЕ ДАННЫЕ")
user_data = {desc: input(f"{desc.upper():16} : ").lower() for desc in user_desc}
print(printout_udata(surname=user_data['фамилия'], name=user_data['имя'], birth_year=user_data['год рождения'],
               phone=user_data['телефон'], city=user_data['город проживания'], email=user_data['email']))
