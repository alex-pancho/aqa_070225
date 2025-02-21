# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for latter in "Hello world!":
    print(latter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)



#task 07
#У саду посадили 4 яблуні.Груш на 5 більше яблунь, а слив - на 2 менше.
#Скільки всього дерев посадили в саду?

apple = 4
pear = apple + 5
plum = apple - 2
trees_at_all = apple + pear + plum
print (trees_at_all)


# task 08
# До обіда температура повітря була на 5 градусів вище нуля.
# Після обіду температура опустилася на 10 градусів.Надвечір потепліло на 4 градуси. 
# Яка температура надвечір?

morning = 0 + 5
day = morning - 10
evening = day + 4
print (evening)

# task 09
# Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
# 1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
# Скількі сьогодні дітей у театральному гуртку?

boys = 24
girls = boys / 2
sick_boys = 1
sick_girls = 2

boys_present = boys - sick_boys
girls_present = girls - sick_girls

tottal = boys_present + girls_present
print (tottal)

# task 10
# Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
# а третя - як половина вартості першої та другої разом.
# Скільки будуть коштувати усі книги, якщо купити по одному примірнику?

book1 = 8
book2 = book1 / 2
book3 = book1 / 2 + book2 / 2
for_3 = book1 + book2 + book3
print(for_3)