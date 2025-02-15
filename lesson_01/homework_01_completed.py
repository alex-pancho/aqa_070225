TASK_START_TEMPLATE = "\n\n---Task {0}---\n"
def print_task(task_number):
    print(TASK_START_TEMPLATE.format(task_number))

# task 01 == Виправте синтаксичні помилки
print_task(1)
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
print_task(2)
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
print_task(3)
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
print_task(4)
apples = 2
banana = 4 * apples
print(f"Apples: {apples}, \nBanana: {banana}")

# task 05 == виправте назви змінних
print_task(5)
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
print_task(6)
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(f"Периметр = {perimetery}")


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
print_task(7)
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше. 
Скільки всього дерев посадили в саду?
"""  # Як на  мене треба уточнити слив менше ніж  яблунь чи груш?

print(
    "Задача:\nУ саду посадили 4 яблуні. "
    "Груш на 5 більше яблунь, а слив - на 2 менше. "
    "Скільки всього дерев посадили в саду?"
)
apples = 4
pears = apples + 5
plums = apples - 2
trees = apples + pears + plums
print(
    f"Дано:\nЯблуні - {apples}.\nГруші - {apples} + 5 = {pears}.\nСливи - {apples} - 2 = {plums}.\n"
    f"В саду посаджено {apples} яблуні, {pears} груш та {plums} сливи.\n"
    f"Розв'язок: {apples} + {pears} + {plums} = {trees} \nВідповідь: Всього в саду посадили - {trees} дерев."
)

# task 08
print_task(8)
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""

print(
    "Задача:\nДо обіда температура повітря була на 5 градусів вище нуля. "
    "Після обіду температура опустилася на 10 градусів. "
    "Надвечір потепліло на 4 градуси. Яка температура надвечір?"
)
morning = 5
day = morning - 10
evening = day + 4
print(
    f"Дано:\nДо обіду - {morning}°C.\nПісля обіду - {morning}°C - 10°C = {day}°C.\nНадвечір - {day}°C + 4°C = {evening}°C.\n"
    f"Відповідь: Температура надвечір = {evening}°C"
)

# task 09
print_task(9)
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""  # Помилка в слові "Скільки"
print(
    "Задача:\nВзагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше. "
    "1 хлопчик захворів та 2 дівчинки не прийшли сьогодні. "
    "Скільки сьогодні дітей у театральному гуртку?"
)
total_boys = 24
total_girls = total_boys // 2
absent_boys = 1
absent_girls = 2
present_boys = total_boys - absent_boys
present_girls = total_girls - absent_girls
present_kids = present_boys + present_girls
print(
    f"Дано:\nВсього хлопчиків - {total_boys} \nВсього дівчат - {total_boys} / 2 = {total_girls}\n"
    f"Захворіли - {absent_boys} хлопчик та {absent_girls} дівчинки \n"
    f"Розв'язок: \n"
    f"{total_boys} - {absent_boys} = {present_boys} хлопчики \n{total_girls} - {absent_girls} = {present_girls} дівчинок\n"
    f"{present_boys} + {present_girls} = {present_kids}\n"
    f"Ввідповідь: Сьогодні у театральному гуртку {present_kids} дитини"
)

# task 10
print_task(10)
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
print(
    "Задача:\nПерша книжка коштує 8 грн., друга - на 2 грн. дороже, "
    "а третя - як половина вартості першої та другої разом. "
    "Скільки будуть коштувати усі книги, якщо купити по одному примірнику?"
)
book_1 = 8
book_2 = book_1 + 2
book_3 = (book_1 + book_2) / 2
formatted_book_3 = int(book_3) if book_3.is_integer() else book_3
total_book = book_1 + book_2 + formatted_book_3
print(
    f"Дано:\nПерша книга: {book_1} грн.\n"
    f"Друга книга: {book_1} + 2 = {book_2} грн.\n"
    f"Третя книга: ({book_1} + {book_2}) / 2 = {formatted_book_3} грн.\n"
    f"Розв'язок:\n{book_1} + {book_2} + {formatted_book_3} = {total_book}\n"
    f"Відповідь: Якщо купити усі книги по одному примірнику, вони коштуватимуть {total_book} грн."
)
