# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті \'
# task 03 == Виведіть змінну alice_in_wonderland на друк
print("________tasks 01-03__________")
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '—— so long as I get somewhere," Alice added as an explanation.\n'
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
print("________task 04__________")
black_sea_area = 436_402
azov_sea_area = 37_800
black_and_azov_sea_area = black_sea_area + azov_sea_area
print(f"Загальна площа Чорного та Азовського морів становить: {black_and_azov_sea_area} км2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
print("________task 05__________")
all_items = 375_291
first_and_second_storages_items = 250_449
second_and_third_storages_items = 222_950
first_items_storage = all_items - second_and_third_storages_items
print(f"На першому складі перебуває: {first_items_storage} товарів.")
third_items_storage = all_items - first_and_second_storages_items
print(f"На третьому складі перебуває: {third_items_storage} товарів.")
second_items_storage = all_items - (first_items_storage + third_items_storage)
print(f"На другому складі перебуває: {second_items_storage} товарів.")
print(f"Перевірка себе. Підрахуємо суму товарів на трьох складах, склавши суму товарів кожного магазину:\n"
      f"На всіх складах {(first_items_storage + second_items_storage + third_items_storage)} товарів")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print("________task 06__________")
loan_term_month = 18
monthly_payment = 1179
price_of_computer = loan_term_month * monthly_payment
print(f"Вартість комп’ютера становить: {price_of_computer} грн.")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("________task 07__________")

division_remainder_a = 8019 % 8
division_remainder_b = 9907 % 9
division_remainder_c = 2789 % 5
division_remainder_d = 7248 % 6
division_remainder_e = 7128 % 5
division_remainder_f = 19224 % 9

print(f"Остача від ділення чисел:\n"
      f"a = {division_remainder_a}\n"
      f"b = {division_remainder_b}\n"
      f"c = {division_remainder_c}\n"
      f"d = {division_remainder_d}\n"
      f"e = {division_remainder_e}\n"
      f"f = {division_remainder_f}\n")

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
print("________task 08__________")

# ціни на товари
pizza_large_price = 274
pizza_medium_price = 218
juice_price = 35
cake_price = 350
water_price = 21

# кількість кожного товару
pizza_large_quantity = 4
pizza_medium_quantity = 2
juice_quantity = 4
cake_quantity = 1
water_quantity = 3

# розразунок загальної вартості всіх товарів
total_price = (pizza_large_price * pizza_large_quantity) + (pizza_medium_quantity * pizza_medium_price) + (
            juice_price * juice_quantity) + (cake_price * cake_quantity) + (water_quantity * water_price)
print(f"Вартість всього замовлення: {total_price} грн.")
# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print("________task 09__________")
all_photo = 232
photos_per_page = 8

# розрахунок кількості сторінок, що потрібні для заданої кількості фоток
all_pages = all_photo // photos_per_page

if all_photo % photos_per_page != 0:
    all_pages += 1

print(f"Ігорю знадобиться {all_pages} сторінок")


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
print("________task 10__________")

# дані із задачі
all_distance = 1600
fuel_consumption = 9
distance_for_fuel_consumption = 100
tank_volume = 48

# розрахунок палива на всю відстань
all_fuel = (all_distance/distance_for_fuel_consumption)*fuel_consumption
print(f"На всю подорож потрібно: {all_fuel} палива.")

# розрахунок кількості зупинок на заправках
refuel_stops = all_fuel // tank_volume
if all_fuel % tank_volume != 0:
    refuel_stops = refuel_stops + 1
print(f"Кількість зупинок на дозаправку = {int(refuel_stops)}")