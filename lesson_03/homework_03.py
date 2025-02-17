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
square_black_sea = 436_402
square_azov_sea = 37_800

total_square_sea = square_black_sea + square_azov_sea
print(f"Чорне та Азовське моря разом займають {total_square_sea} км2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_goods = 375_291
first_second_goods = 250_449
second_third_goods = 222_950

first_goods = total_goods - second_third_goods
second_goods = first_second_goods - first_goods
third_goods = total_goods - first_goods - second_goods
print(f"На першому складі {first_goods} товарів, на другому {second_goods}, на третьому {third_goods}")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
mountly_payment = 1179
total_months = 12 * 1.5

total_price = mountly_payment * total_months
print(f"Вартість комп'ютера становить {total_price} грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print(f"a) {8019 % 8}", end="     ")
print(f"d) {7248 % 6}")
print(f"b) {9907 % 9}", end="     ")
print(f"e) {7128 % 5}")
print(f"c) {2789 % 5}", end="     ")
print(f"f) {19224 % 9}")

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

total_order = (pizza_large_price * pizza_large_quantity +
               pizza_medium_price * pizza_medium_quantity +
               juice_price * juice_quantity +
               cake_price * cake_quantity +
               water_price * water_quantity)
print(f"Іринці знадобиться {total_order} грн для замовлення")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos = 232
photos_per_page = 8

if photos % photos_per_page == 0:
    total_pages = photos // photos_per_page
else:
    total_pages = photos // photos_per_page + 1
print(f"Ігорю знадобиться {total_pages} сторінок для вклеювання фото")

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
distance = 1600
fuel_consumption = 9
tank_capacity = 48

total_fuel = distance / 100 * fuel_consumption
if total_fuel % tank_capacity == 0:
    total_refills = total_fuel // tank_capacity
else:
    total_refills = total_fuel // tank_capacity + 1
print(f"1) Для подорожі знадобиться {total_fuel} літрів бензину")
print(f"2) Родині необхідно заїхати на заправку {total_refills} разів")
