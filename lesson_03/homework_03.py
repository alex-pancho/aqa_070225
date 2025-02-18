import math 
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

#Task 01
alice_in_wonderland = """
"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where —" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."
"""

#Task 02 

apostrophes = [char for char in alice_in_wonderland if char == "'"]
apostrophes_indexes = [i for i,char in enumerate(alice_in_wonderland) if char == "'"]
print(f"Found apostrophes {apostrophes}, with indexes {apostrophes_indexes}")

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

square_of_black_sea = 436402
square_of_azov_sea = 37800
square_of_black_and_azov_seas = square_of_black_sea + square_of_azov_sea
print(f"Total square of Black and Azov sea --> {square_of_black_sea} + {square_of_azov_sea} = {square_of_black_and_azov_seas}")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_amount_of_goods = 375291
amount_in_first_and_second_warehouse = 250449
amount_in_second_and_third_warehouse = 222950
amount_in_first_warehouse = total_amount_of_goods - amount_in_second_and_third_warehouse
amount_in_third_warehouse = total_amount_of_goods - amount_in_first_and_second_warehouse
amount_in_second_warehouse = total_amount_of_goods - amount_in_first_warehouse - amount_in_third_warehouse
print(f"Amount of goods for each warehouse: Firts = {amount_in_first_warehouse}, Second = {amount_in_second_warehouse}, Third = {amount_in_third_warehouse}") 

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

payment_time_in_months = 18
payment_per_month_in_uah = 1179
pc_cost = payment_time_in_months * payment_per_month_in_uah
print(f"Total cost of pc will be {pc_cost} uah")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
    
print("Reminder from 8019 % 8 is", 8019 % 8)
print("Reminder from 9907 % 9 is", 9907 % 9)
print("Reminder from 2789 % 5 is", 2789 % 5)
print("Reminder from 7248 % 6 is", 7248 % 6)
print("Reminder from 7128 % 5 is", 7128 % 5)
print("Reminder from 19224 % 9 is", 19224 % 9)


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


pizza_big = 4 * 274
pizza_medium = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21

total = pizza_big + pizza_medium + juice + cake + water

print("Загальна сума: ", total, "грн")


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos = 232
page_in_album = 8
pages_needed = math.ceil(photos / page_in_album)
print(f"Igor needs {pages_needed} to fit all of the {photos} photos")


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
cosnumption_per_100 = 9
tank = 48
gas_needed_to_travel = (distance / 100) * cosnumption_per_100
times_to_tank = math.ceil(gas_needed_to_travel / tank)
print(f"For this journey family need {gas_needed_to_travel} liters of gas and tank it {times_to_tank} times")

