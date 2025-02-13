# task 01 == Виправте синтаксичні помилки
print("Task 1")

print("Hello", end = " ")
print("world!")


# task 02 == Виправте синтаксичні помилки
print("Task 2")

hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
print("Task 3")

for letter in "Hello world!":
    print(letter, end="")
print()

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук

apples = 2
banana = apples * 4


# task 05 == виправте назви змінних
side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для к
# ористувача
print("Task 6")
perimeter = side_1 + side_2 + side_3 + side_4 
print(f"Периметр фігури з задання 5 доівнює {perimeter}.")


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""

# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в сад?
"""
print("Task 07")

apples = 4

print("1. Скільки груш посадили?")
pears = apples + 5
print(f"{apples} + 5 = {pears} (груш)")

print("2. Скільки посадили слив?")
plums = apples - 2
print(f"{apples} - 2 = {plums} (слив)")

print("3. Скільки всього дерев посадили в саду?")
trees = apples + pears + plums
print(f"{apples} +  {pears} + {plums} = {trees} (дерев)")

print(f"Відповідь: Всього  в саду посадили {trees} дерев.")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
print("Task 08")

temperature_morning = 5

print(f"1. Яка температува після обіду?")
temperature_afternoon = temperature_morning - 10
print(f"{temperature_morning} - 10 = {temperature_afternoon}°")

print(f"2. Яка температува надвечі?")
temperature_evening = temperature_afternoon + 4
print(f"{temperature_afternoon} + 4 = {temperature_evening}°")

print(f"Відповідь: Tемпература  повітря надвечір {temperature_evening}°.")


# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
print("Task 09")

boys = 24

print("1. Скільки дівчат у гуртку?")
girls = boys // 2
print(f"{boys} : 2 = {girls} (дівчат)")

print("2. Скільки хлопців у гуртку сьогодні?")
boys_today = boys-1
print(f"{boys} - 1 = {boys_today} (хлопців сьогодні)")

print("3. Скільки дівчат у гуртку сьогодні")
girls_today = girls - 2
print(f"{girls} - 2 = {girls_today} (дівчат сьогодні)")

print("4. Скількі сьогодні дітей у театральному гуртку?")
kids_today = boys_today + girls_today
print(f"{boys_today} + {girls_today} = {kids_today} (дітей)")

print(f"Відповідь: Cьогодні у театральному гуртку {kids_today} дітей.")


# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
print("Task 10")
price_book_1 = 8

print("Скільки коштує друга книга?")
price_book_2 = price_book_1 + 2
print(f"{price_book_1} + 2 + {price_book_2} грн")

print("2. Скільки коштує перша та друга книги разом?")
price_book_1_and_2 = price_book_1 + price_book_2
print(f"{price_book_1} + {price_book_2} = {price_book_1_and_2} грн.")

print("Скільки коштує третя книга?")
price_book_3 = price_book_1_and_2 // 2
print(f"{price_book_1_and_2} : 2 = {price_book_2} грн.")

print("Скільки будуть коштувати усі книги, якщо купити по одному примірнику?")
price_books = price_book_1 + price_book_2 + price_book_3
print(f"{price_book_1} + {price_book_2} + {price_book_3} = {price_books} грн.")

print(f"Відповідь: Вартість усіх книг, якщо купити по одному примірнику становить {price_books} грн.")