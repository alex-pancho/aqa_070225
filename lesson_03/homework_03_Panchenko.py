# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті

alice_in_wonderland = "\"Would you tell me, please, which way I ought to go from here?\" \n\
\"That depends a good deal on where you want to get to,\" said the Cat. \n\
\"I don\'t much care where ——\" said Alice. \n\
\"Then it doesn\'t matter which way you go,\" said the Cat. \n\
\"—— so long as I get somewhere,\" Alice added as an explanation. \n\
\"Oh, you\'re sure to do that,\" said the Cat, \"if you only walk long enough.\""

# task 03 == Виведіть змінну alice_in_wonderland на друк

print (alice_in_wonderland)

#tasks 1-3 == альтернатива
alice_in_wonderland2 = """\"Would you tell me, please, which way I ought to go from here?\" 
\"That depends a good deal on where you want to get to,\" said the Cat. 
\"I don\'t much care where ——\" said Alice. 
\"Then it doesn\'t matter which way you go,\" said the Cat. 
\"—— so long as I get somewhere,\" Alice added as an explanation. 
\"Oh, you\'re sure to do that,\" said the Cat, \"if you only walk long enough.\""""

print(alice_in_wonderland2)

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

area_of_the_black_sea = 436402
area_of_the_sea_of_azov = 37800 

total_sea_area = area_of_the_black_sea + area_of_the_sea_of_azov

print (f"total sea area: {total_sea_area} km2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

def goods():
    total = 375291
    first_and_second = 250449
    second_and_third = 222950
    y = (total - first_and_second + second_and_third) // 2
    x = first_and_second - y
    z = second_and_third - y
    return x, y, z

x, y, z = goods()
print(f"on first warehouse: {x}")
print(f"on second warehouse: {y}")
print(f"on second warehouse: {z}")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

monthly_payment = 1179
months = 12 + (12 / 2)

total_cost = monthly_payment * months

print(f"total cost: {total_cost}")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

a = 8019 % 8
b = 9907 % 9
c = 2786 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print(f"remainder of division {a}")
print(f"remainder of division {b}")
print(f"remainder of division {c}")
print(f"remainder of division {d}")
print(f"remainder of division {e}")
print(f"remainder of division {f}")

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

pizza_large = 4
pizza_medium = 2
juice = 4
cake = 1
water = 3

pizza_large_price = 274
pizza_medium_price = 218
juice_price = 35
cake_price = 350
water_price = 21

total_cost = (pizza_large * pizza_large_price) + \
             (pizza_medium * pizza_medium_price) + \
             (juice * juice_price) + \
             (cake * cake_price) + \
             (water * water_price)

print(f"total cost: {total_cost}")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

fotos = 232
fotos_per_page = 8
number_of_pages = fotos / fotos_per_page

print(f"pages needed: {number_of_pages}")

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
tank_capacity = 48
l_per_100km = 9
km_per_9l = 100
distanse_per_tank = ((tank_capacity // l_per_100km) * km_per_9l)
stops = distance // distanse_per_tank
total_fuel = ((distance // km_per_9l) * l_per_100km)

print(f"total fuel used: {total_fuel}")
print(f"total number of stops: {stops}")