# Проект FitLife - MVP версия 2.0
# Пропишем константы
WATER_PER_KG = 30
MILLILITERS_IN_LITER = 1000
# Знакомство. Узнаем имя
user_name = input('Здравствуйте! Я рад стать вашим помощником. Как вас зовут?')
user_name = user_name.title()  # Возводит имя в верхний регистр
# Узнаем возраст
user_age = input('Сколько вам лет? ')


def correct_age(user_age):
    """преобразует в число с плавоющей точкой, меняет запятую на точку"""
    try:
        return float(user_age)
    except ValueError:
        return float(user_age.replace(',', '.'))


final_age = int(correct_age(user_age))  # Преобразуем в число
# Узнаем вес
user_weight = input('Укажите свой вес в килограммах, например: 63.6 ')


def correct_weight(user_weight):
    """преобразует в число с плавающей точкой, меняет запятую на точку"""
    try:
        return float(user_weight)
    except ValueError:
        return float(user_weight.replace(',', '.'))


user_height = input('Укажите свой рост в метрах, например: 1.75 ')


def correct_height(user_height):
    """преобразует в число с плавающей точкой, меняет запятую на точку"""
    try:
        return float(user_height)
    except ValueError:
        return float(user_height.replace(',', '.'))


# Расчет индекса массы тела
bmi = correct_weight(user_weight) / (correct_height(user_height) ** 2)
# Расчет нормы воды
water_l = correct_weight(user_weight) * WATER_PER_KG / MILLILITERS_IN_LITER
print('-' * 40)
print(f'Отчет для пользователя: {user_name} ({final_age} лет)')
print(f'{user_name} ваш Индекс Массы Тела: {bmi:.1f}')
print(f'Рекомендуемая норма воды: {water_l:.1f} л. в день')
print('Расчет окончен. Будьте здоровы!')
