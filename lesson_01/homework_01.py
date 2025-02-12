# task 01 == Виправте синтаксичні помилки
print("Hello world")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if hello:
   print(f"{hello} {world}")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!": # по одній букві, бо є for - це цикл, ітерації елементів
   print(letter)

# task 04 == Зробіть так, щоб кількість бананів була завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4 
print (banana)

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05 та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(f"Параметр фігури: {perimetery}")


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
tree_apple = 4
tree_pear = tree_apple + 5 
tree_plums = tree_apple - 2 
total_tree = tree_apple + tree_pear + tree_plums 
print(f"Всього {total_tree} дерев посадили в саду")

# task 08
"""
#До обіда температура повітря була на 5 градусів вище нуля.
#Після обіду температура опустилася на 10 градусів.
#Надвечір потепліло на 4 градуси. Яка температура надвечір?
#"""

temperature_morning = + 5
temperature_afternoon = temperature_morning - 10
temperature_evening = temperature_afternoon + 4
print (f"Температура надвечір {temperature_evening} градус")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = boys // 2
boy_sick = 1
girls_absent = 2
total_children_today = boys - boy_sick + girls - girls_absent
print (f"Сьогодні до театрального гуртка прийшло, {total_children_today} дитини")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book1_cost = 8
book2_cost = book1_cost + 2
book3_cost = (book1_cost + book2_cost) // 2 
total_cost = book1_cost + book2_cost + book3_cost
print (f"Усі книги будуть коштувати, {total_cost} грн., якшо купити по одному примірнику")
