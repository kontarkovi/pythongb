# УРОК 1. ЗАДАНИЕ 2
"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк
"""
time = input("Введите время в секундах: ")
if time.isdigit():
    sec_time = int(time)
    if 0 <= sec_time <= 86400:  # В сутках 86400 секунд
        hours = sec_time // 3600  # В часе 3600 секунд
        minutes = (sec_time % 3600) // 60  # В минуте 60 секунд
        seconds = (sec_time % 3600) - (minutes * 60)
        print(f"Время в формате чч:мм:сс составляет: {hours:0>2d}:{minutes:0>2d}:{seconds:0>2d}")
    else:
        print("Временной период охватывает более суток!")
else:
    print("Введите неотрицательное целое число!")