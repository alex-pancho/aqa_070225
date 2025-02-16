alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."
'''

print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


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

area_black_sea = 436_402
area_azov_sea = 37_800
area_sum = area_black_sea + area_azov_sea
print(f"Чорне та Азовське моря разом займають {area_sum} км2.\n")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

storage_sum = 375_291
storage_first_and_second = 250_449
storage_second_and_third = 222_950
storage_third = storage_sum - storage_first_and_second
storage_second = storage_second_and_third - storage_third
storage_first = storage_first_and_second - storage_second

print(
    f"На першому складі {storage_first} товарів, на другому складі "
    f"{storage_second} товарів, на третьому складі {storage_third} товарів.\n")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
payment_per_month = 1179
sum_of_month = 18
price_of_computer = payment_per_month * sum_of_month

print(f"Комп'ютер коштує {price_of_computer} грн.\n")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
example_a = 8019 // 8
example_b = 9907 // 9
example_c = 2789 // 5
example_d = 7248 // 6
example_e = 7128 // 5
example_f = 19224 // 9

example_a_remainder = 8019 % 8
example_b_remainder = 9907 % 9
example_c_remainder = 2789 % 5
example_d_remainder = 7248 % 6
example_e_remainder = 7128 % 5
example_f_remainder = 19224 % 9
print(f"a) 8019 : 8 = {example_a} (ост. {example_a_remainder})\n"
      f"b) 9907 : 9 = {example_b} (ост. {example_b_remainder})\n"
      f"c) 2789 : 5 = {example_c} (ост. {example_c_remainder})\n"
      f"d) 7248 : 6 = {example_d} (ост. {example_d_remainder})\n"
      f"e) 7128 : 5 = {example_e} (ост. {example_e_remainder})\n"
      f"f) 19224 : 9 = {example_f} (ост. {example_f_remainder})\n")

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
all_products_price = (big_pizza_price * big_pizza_amount +
                      medium_pizza_price * medium_pizza_amount +
                      juice_price * juice_amount +
                      cake_price * cake_amount +
                      water_price * water_amount)
print(f"Іринці знадобиться {all_products_price} грн для сплати замовлення\n")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_pictures = 232
page_size = 8
if all_pictures % page_size == 0:
    all_page = (232 // 8)
else:
    all_page = (232 // 8) + 1
print(f"Ігорю знадобиться {all_page} сторінок\n")

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
segment_length = 100
segment_fuel = 9
tank_capacity = 48
all_distance_fuel = distance / segment_length * segment_fuel
all_fuel_stop = all_distance_fuel / tank_capacity
print(f"1) Для такої подорожі знадобиться {all_distance_fuel} літри\n"
      f"2) Щонайменше родині необхідно заїхати на заправку {all_fuel_stop} рази\n")
