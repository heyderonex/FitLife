# Проект FitLife - MVP версия 1.0
print("Вас приветствует виртуальный помощник FitLive")
print("Я могу посчитать ваш ИМТ(индекс массы тела) и норму воды в день")
print("Для этого мне нужно немного информации о вас")
user_name = input("Введите ваше имя: ")
user_age = int(input("Введите ваш возраст: "))
user_weight = float(input("Введите ваш вес(кг): "))
user_height = float(input("Введите ваш рост(м): "))
bmi = round(user_weight / (user_height ** 2), 1)
water_ml = user_weight * 30
water_l = water_ml / 1000
print(f"\nОтчет для пользователя: {user_name}, {user_age} г.")
print(f"Индекс массы тела: {bmi}")
print(f"Норма воды: {water_l}л в день")
print(f"\nРасчет окончен. Будьте здоровы!")
