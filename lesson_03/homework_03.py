alice_in_wonderland = (
    'Would you tell me, please, which way I ought to go from here?\n'
    'That depends a good deal on where you want to get to, said the Cat.\n'
    'I don\'t much care where —— said Alice.\n'
    'Then it doesn\'t matter which way you go, said the Cat.\n'
    '—— so long as I get somewhere, Alice added as an explanation.\n'
    'Oh, you\'re sure to do that, said the Cat, if you only walk long enough.'
)
print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті \'
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
black_sea = 436402
azov_sea = 37800
total_sea = black_sea + azov_sea
print(f"Площа Чорного та Азовського моря", total_sea, "км2")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_goods = 375291
first_second_goods = 250449
second_third_goods = 222950
first_goods = total_goods - second_third_goods
second_goods = first_second_goods - first_goods
third_goods = total_goods - first_goods - second_goods
print(f"Знайдіть кількість товарів на складі", first_goods)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment = 1179
total_payment = monthly_payment * 18
print(f"Вартість компʼютера {total_payment}")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print("a=", a, "b=", b, "c=", c, "d=", d, "e=", e, "f=", f)


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
big_pizza = 274
medium_pizza = 218
juice = 35
cake = 350
water = 21
total_order = big_pizza * 4 + medium_pizza * 2 + juice * 4 + cake + water * 3
print(total_order, "грошей знадобиться для даного її замовлення")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos = 232
photos_per_page = 8
pages = photos // photos_per_page
if photos % photos_per_page:
    pages += 1
print(pages, "сторінок знадобиться Ігорю, щоб вклеїти всі фото")



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
fuel_per_100_km = 9
tank_capacity = 48
fuel = distance / 100 * fuel_per_100_km
print(fuel, "літрів бензину знадобиться для такої подорожі")
refills = fuel // tank_capacity
if fuel % tank_capacity:
    refills += 1
print(refills, "разів родині необхідно заїхати на заправку під час цієї подорожі, кожного разу заправляючи повний бак")