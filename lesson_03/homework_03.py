alice_in_wonderland = """Would you tell me, please, which way I ought to go from here?
That depends a good deal on where you want to get to, said the Cat.
I don't much care where —— said Alice.
Then it doesn't matter which way you go, said the Cat.
—— so long as I get somewhere, Alice added as an explanation.
Oh, you're sure to do that, said the Cat, if you only walk long enough."""
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


for x in alice_in_wonderland:
    if x == "'":
       print(x)

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
plosha_chorne_more = 436402 
plosha_azovske_more = 37800 

# Обчислення
zag_plosha = plosha_chorne_more + plosha_azovske_more

# Виведення
print(f"Разом Чорне та Азовське моря займають {zag_plosha} км².")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
# Дано
zag_tovary = 375291
sklad1_sklad2 = 250449  
sklad2_sklad3 = 222950  

# Обчислення 
sklad2 = (sklad1_sklad2 + sklad2_sklad3 - zag_tovary) // 2
sklad1 = sklad1_sklad2 - sklad2
sklad3 = sklad2_sklad3 - sklad2

# Виведення
print(f"На першому складі: {sklad1} товарів.")
print(f"На другому складі: {sklad2} товарів.")
print(f"На третьому складі: {sklad3} товарів.")


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
# Дано
misyatsiv = 1.5 * 12 
oplata_za_misyats = 1179

# Обчислення
vartist_komp = misyatsiv * oplata_za_misyats

# Виведення
print(f"Вартість комп'ютера: {vartist_komp} грн.")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
# Дано
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

# Виведення
print(f"a) 8019 : 8, остача = {a}")
print(f"b) 9907 : 9, остача = {b}")
print(f"c) 2789 : 5, остача = {c}")
print(f"d) 7248 : 6, остача = {d}")
print(f"e) 7128 : 5, остача = {e}")
print(f"f) 19224 : 9, остача = {f}")


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
pitsa_velyka = 4 * 274
pitsa_serednya = 2 * 218
sik = 4 * 35
tort = 1 * 350
voda = 3 * 21

# Обчислення
zag_vartist = pitsa_velyka + pitsa_serednya + sik + tort + voda

# Виведення 
print(f"Загальна сума замовлення: {zag_vartist} грн.")


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
# Дано
foto_zagalom = 232
foto_na_storinku = 8

# Обчислення
storinky_potribno = -(-foto_zagalom // foto_na_storinku)

# Виведення
print(f"Ігорю знадобиться {storinky_potribno} сторінок для вклеювання всіх фото.")


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
vidstan = 1600
vtrata_na_100_km = 9
mistkist_baka = 48

# Обчислення
potreben_benzyn = (vidstan / 100) * vtrata_na_100_km
zapravky = -(-potreben_benzyn // mistkist_baka)

# Виведення 
print(f"1) Для подорожі потрібно {potreben_benzyn} літрів бензину.")
print(f"2) Родині потрібно заїхати на заправку щонайменше {int(zapravky)} рази(-ів).")
