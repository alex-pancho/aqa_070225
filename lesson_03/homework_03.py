#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті \'
# task 03 == Виведіть змінну alice_in_wonderland на друк
print ('Task 1 ')
alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'''
print(alice_in_wonderland)


print ('\nTask 2 ')
alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
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
print ('\nTask 4 ')
black_sea_area =436402
asov_sea_area =37800
print("Яку площу займають Чорне та Азов-ське моря разом?")
print(f"{black_sea_area}+{asov_sea_area}={black_sea_area+asov_sea_area}")   
print(f"Відповідь: {black_sea_area+asov_sea_area}км2")   

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
print ('\nTask 5 ')
total_products = 375291
products_at_1_2 = 250449
products_at_2_3 = 222950
print("Скільки товарів на першому складі?")
print(f"{total_products}-{products_at_2_3}={total_products-products_at_2_3}")   
print("Скільки товарів на другому складі?")
print(f"{products_at_1_2}-{total_products-products_at_2_3}="
      f"{products_at_1_2-(total_products-products_at_2_3)}")   
print("Скільки товарів на третьому складі?")
print(f"{total_products}-{products_at_1_2}={total_products-products_at_1_2}")   
print(f"Відповідь: На 1, 2 та 3 складах {total_products-products_at_2_3}, "
      f"{products_at_1_2-(total_products-products_at_2_3)}, "
      f"{total_products-products_at_1_2} товарів відповідно") 



# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print ('\nTask 6')
period = 18
monthly_payment = 11798
print("Яка вартість комп’ютера?")
print(f"{period}*{monthly_payment}={period*monthly_payment}")   
print(f"Відповідь: Вартість комп’ютера {period*monthly_payment} грн") 

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print ('\nTask 7')
print(f"a. Остача від ділення 8019:8 дорівнює {8019%8}")
print(f"b. Остача від ділення 9907:9 дорівнює {9907%9}")
print(f"c. Остача від ділення 2789:5 дорівнює {2789%5}")
print(f"d. Остача від ділення 7248:6 дорівнює {7248%6}")
print(f"e. Остача від ділення 7128:5 дорівнює {7128%5}")
print(f"f. Остача від ділення 19224:9 дорівнює {19224%9}")


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
print ('\nTask 8')
pizza_L_price = 274
pizza_M_price = 218
juice_price = 35
cake_price = 350
water_price = 21

pizza_L_quantity = 4
pizza_M_quantity = 2
juice_quantity = 4
cake_quantity = 1
water_quantity = 3

total_price = (pizza_L_price * pizza_L_quantity + 
               pizza_M_price * pizza_M_quantity + 
               juice_price * juice_quantity + 
               cake_price * cake_quantity + 
               water_price * water_quantity)

print("Cкільки грошей знадобиться для даного замовлення?")
print(f"{pizza_L_price}*{pizza_L_quantity}+{pizza_M_price}*{pizza_M_quantity}+"
      f"{juice_price}*{juice_quantity}+{cake_price}*{cake_quantity}+"
      f"{water_price}*{water_quantity}={total_price}")
print(f"Відповідь: Вартість замовлення {total_price} грн") 


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print ('\nTask 9')
total_pic = 232
pic_per_page = 8

"""Для того, щоб поділити число і заокруглити його до більшого цілого, 
можна скористатися функцією math.ceil() з модуля math, або за допомогою цілочисельного ділення
result = -(-7 // 3) 
print(result) Виведе 3 """

pages_needed = -(-total_pic // pic_per_page) 
print("Скільки сторінок знадобиться, щоб вклеїти всі фото?")
print(f"{total_pic}/{pic_per_page}={pages_needed}")   
print(f"Відповідь: Вартість замовлення {pages_needed} грн") 

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
print ('\nTask 10')
kharkiv_budapest_distance = 1600
gas_for_100_km = 9
tank_capacity = 48

fuel_for_one_way_trip = kharkiv_budapest_distance / 100 * gas_for_100_km
print("Скільки літрів бензину знадобиться для подорожі до Будапешту?")
print(f"{kharkiv_budapest_distance}/100*{gas_for_100_km}={fuel_for_one_way_trip}")
refill_count = int(-(-fuel_for_one_way_trip//tank_capacity))
print("Скільки разів родині необхідно заїхати на заправку для подорожі до Будапешту?")
print(f"{fuel_for_one_way_trip}/{tank_capacity}={refill_count}")

print(f"Відповідь: Для подорожі в одну сторону необхідно {fuel_for_one_way_trip} л. пального"
      f"та {refill_count} рази запрвити авто.") 