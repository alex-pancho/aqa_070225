adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while 
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# task 01 ==
print("_______________task 01____________________")
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print("Замінені переноси строки на пробіл: ", adwentures_of_tom_sawer)

# task 02 ==
print("_______________task 02____________________")
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print("Замінені символи '....' на пробіл: ", adwentures_of_tom_sawer)

# task 03 ==
print("_______________task 03____________________")
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
split_text = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = ' '.join(split_text)
print("Видален зайві пробіли:", adwentures_of_tom_sawer)

# task 04
print("_______________task 04____________________")
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count = adwentures_of_tom_sawer.count("h")
print("Літера 'h' зустрічається в тексті:", count, "разів.")

# task 05
print("_______________task 05____________________")
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
counter = 0
for i in adwentures_of_tom_sawer:
    if i.isupper():
        counter = counter + 1

print("У тексті", counter, "великих літер")

# task 06
print("_______________task 06____________________")
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
index = adwentures_of_tom_sawer.find("Tom")  # знайшли входження Тома 1 раз
next_index = adwentures_of_tom_sawer.find("Tom", index + 1)  # шукаємо наступне входження по індексу
print(f"Слово 'Tom' вдруге зустрічається на {next_index} індексі строки")
print("Виведемо зріз із трьох символів, починаючи зі знайденого індекса: ", adwentures_of_tom_sawer[439:442])  # вивід
# для себе, щоб переконатись що значення знайдене вірне

# task 07
print("_______________task 07____________________")
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")
print("Розбитий по реченням текст: ", adwentures_of_tom_sawer_sentences)

# task 08
print("_______________task 08____________________")
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_element = adwentures_of_tom_sawer_sentences[3]
fourth_string = fourth_element.lower()
print("Четверте речення у нижньому регістрі: ", fourth_string)

# task 09
print("_______________task 09____________________")
""" Перевірте чи починається якесь речення з "By the time".
"""
# пройдемось по раніше створеному списку речень adwentures_of_tom_sawer_sentences
for i in adwentures_of_tom_sawer_sentences:
    if i.startswith("By the time"):
        print(f"Є речення, що починається з 'By the time'. Воно звучить так: {i}")

# task 10
print("_______________task 10____________________")
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
# останнє речення = останній елемент списку з реченнями
last_sentance = adwentures_of_tom_sawer_sentences[-1]
# розбиваємо речення на слова
last_sentance_list = last_sentance.split()
# рахуємо довжину списку (кількість елементів списку) - вона ж кількість слів у реченні:
count_of_words = len(last_sentance_list)
print("В останньому реченні:", count_of_words, "слів")
