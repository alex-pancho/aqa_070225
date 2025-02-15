# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"\n
"That depends a good deal on where you want to get to," said the Cat.\n
"I don\'t much care where ——" said Alice.\n
"Then it doesn\'t matter which way you go," said the Cat.\n
"—— so long as I get somewhere," Alice added as an explanation.\n
"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'''

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
black_sea_square = 436_402
azov_sea_square = 37_800

total_sea_square = black_sea_square + azov_sea_square

print(f'Чорне та Азовське моря разом займають {total_sea_square} км2')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_goods_amount = 375_291
first_and_second_store_goods_amount = 250_449
second_and_third_store_goods_amount = 222_950

first_store_goods_amount = total_goods_amount - second_and_third_store_goods_amount
third_store_goods_amount = total_goods_amount - first_and_second_store_goods_amount
second_store_goods_amount = total_goods_amount - first_store_goods_amount - third_store_goods_amount

print(f'''Кількість товарів на першому складі: {first_store_goods_amount} товар.
Кількість товарів на другому складі: {second_store_goods_amount} товар.
Кількість товарів на третьому складі: {third_store_goods_amount} товар. ''')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment = 1179
total_months = 18

computer_price = monthly_payment * total_months

print(f'Вартість комп’ютера становит {computer_price} грн.')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

print(f'Остача від діленя чисел \'8019 : 8\' становить: {8019 % 8}')
print(f'Остача від діленя чисел \'9907 : 9\' становить: {9907 % 9}')
print(f'Остача від діленя чисел \'2789 : 5\' становить: {2789 % 5}')
print(f'Остача від діленя чисел \'7248 : 6\' становить: {7248 % 6}')
print(f'Остача від діленя чисел \'7128 : 5\' становить: {7128 % 5}')
print(f'Остача від діленя чисел \'19224 : 9\' становить: {19224 % 9}')

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

big_pizza_price = 274
big_pizza_amount = 4
medium_pizza_price = 218
medium_pizza_amount = 2
juice_price = 35
juice_amount = 4
cake_price = 350
cake_amount = 1
water_price = 21
water_amount = 3

total_money_amount = (big_pizza_amount * big_pizza_price) + (medium_pizza_amount * medium_pizza_price) + (juice_amount * juice_price) + (cake_amount * cake_price) + (water_amount * water_price)

print(f'Потрібна сума грошей для всього замовлення: {total_money_amount} грн.')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photos_amount = 232
photos_per_page = 8

pages_amount = total_photos_amount / photos_per_page

print(f'Щоб вклеїти всі фото необхідно {pages_amount} сторінок.')

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
trip_distance = 1600
fuel_per_100km_in_liters = 9
tank_capacity_in_liters = 48

total_fuel_needed = trip_distance / fuel_per_100km_in_liters
gas_station_visits = total_fuel_needed / tank_capacity_in_liters

print(f'Всього для подорожі знадобиться {round(total_fuel_needed)} літрів бензину')
print(f'Кількість різів які необхідно заїхати на заправку, кожного разу заправляючи повний бак: {round(gas_station_visits)}')