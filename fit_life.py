# Проект FitLife - MVP версия 1.0
# Пропишем константы
WATER_PER_KG = 30
MILLILITERS_IN_LITER = 1000
# Знакомство. Узнаем имя
user_name = input('Здравствуйте! Я рад стать вашим помощником. Как вас зовут?')
user_name = user_name.title()  # Возводит имя в верхний регистр
# Узнаем возраст
user_age = input('Сколько вам лет? ')
user_age = int(user_age)  # Преобразуем в число
# Узнаем вес
user_weight = input('Укажите свой вес в килограммах, например: 63.6 ')
# Преобразуем в число с плавающей точкой и защищаем от некорректного ввода


def correct_weight(user_weight):
    """преобразует в число с плавающей точкой, меняет запятую на точку"""
    try:
        return float(user_weight)
    except ValueError:
        return float(user_weight.replace(',', '.'))
# Узнаем рост


user_height = input('Укажите свой рост в метрах, например: 1.75 ')
# Преобразуем в число с плавающей точкой и защищаем от некорректного ввода


def correct_height(user_height):
    """преобразует в число с плавающей точкой, меняет запятую на точку"""
    try:
        return float(user_height)
    except ValueError:
        return float(user_height.replace(',', '.'))


# Расчет индекса массы тела
bmi = correct_weight(user_weight) / (correct_height(user_height) ** 2)
# Расчет нормы воды
water_ml = correct_weight(user_weight) * WATER_PER_KG
water_l = water_ml / MILLILITERS_IN_LITER  # Переводим в литры
print(f'Отчет для пользователя: {user_name} ({user_age} лет)')
print(f'{user_name} ваш Индекс Массы Тела: {bmi:.1f}')
print(f'Рекомендуемая норма воды: {water_l:.1f} л. в день')
print('Расчет окончен. Будьте здоровы!')
