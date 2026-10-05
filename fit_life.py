# Проект FitLife - MVP версия 1.0
print("Вас приветствует виртуальный помощник FitLive")
print("Я могу посчитать ваш ИМТ(индекс массы тела) и норму воды в день")
print("Для этого мне нужно немного информации о вас")
print("Введите ваше имя:")
user_name = input()
print("Введите ваш возраст:")
user_age = int(input())
print("Введите ваш вес(кг):")
user_weight = float(input())
print("Введите ваш рост(м): ")
user_height = float(input())
bmi = round(user_weight / (user_height ** 2), 1)
water_ml = user_weight * 30
water_l = water_ml / 1000
print(f"\nОтчет для пользователя: {user_name}, {user_age} г.")
print(f"Индекс массы тела: {bmi}")
print(f"Норма воды: {water_l}л в день")
print("\nРасчет окончен. Будьте здоровы!")
