import math

# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
# Дано
square_black_sea = 436_402
square_azov_sea = 37_800

# Розв'язок
total_square_sea = square_black_sea + square_azov_sea

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
# Дано
total_goods = 375_291
first_second_goods = 250_449
second_third_goods = 222_950

# Розв'язок
first_goods = total_goods - second_third_goods
second_goods = first_second_goods - first_goods
third_goods = total_goods - first_goods - second_goods

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
# Дано
mount_payment = 1179
total_months = 12 * 1.5

# Розв'язок
total_price = mount_payment * total_months

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
# Дано
numbers = [(8019, 8), (9907, 9), (2789, 5), (7248, 6), (7128, 5), (19224, 9)]

# Розв'язок
for dividend, divisor in numbers:
    remainder = dividend % divisor
    print(f"{dividend} : {divisor} -> остача {remainder}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
# Дано
pizza_large_price = 274
pizza_medium_price = 218
juice_price = 35
cake_price = 350
water_price = 21

pizza_large_quantity = 4
pizza_medium_quantity = 2
juice_quantity = 4
cake_quantity = 1
water_quantity = 3

# Розв'язок
total_pizza_large = pizza_large_price * pizza_large_quantity
total_pizza_medium = pizza_medium_price * pizza_medium_quantity
total_juice = juice_price * juice_quantity
total_cake = cake_price * cake_quantity
total_water = water_price * water_quantity

total_order = total_pizza_large + total_pizza_medium + total_juice + total_cake + total_water

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
# Дано
photos = 232
photos_per_page = 8

# Розв'язок
total_pages = math.ceil(photos / photos_per_page)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
# Дано
distance = 1600
fuel_consumption = 9
tank_capacity = 48

# Розв'язок
total_fuel = distance / 100 * fuel_consumption
total_refills = math.ceil(total_fuel / tank_capacity)