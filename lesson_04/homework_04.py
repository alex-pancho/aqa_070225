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

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
split_text = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = " ".join(split_text)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
h_count = adwentures_of_tom_sawer.count("h")
print(f"Літера 'h' зустрічається в тексті {h_count} раз\n")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
capitals_count = sum(1 for i in adwentures_of_tom_sawer if i.isupper())
print(f"{capitals_count} слів починаються з великої літери в тексті\n")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
index_1 = adwentures_of_tom_sawer.find("Tom")
index_2 = adwentures_of_tom_sawer.find("Tom", index_1 + 1)
print(f"Слово Tom вдруге зустрічається на позиції {index_2}\n")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence = adwentures_of_tom_sawer_sentences[3].lower()
print(f"Четверте речення в нижньому регістрі: {fourth_sentence}\n")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
sentence_count = 0
sentence_not_found = True
for i in adwentures_of_tom_sawer_sentences:
    sentence_count += 1
    if i.find("By the time") == 0:
        print(f"Так, {sentence_count} речення")
        sentence_not_found = False
if sentence_not_found:
    print(f"Ні, жодне речення не починається з 'By the time'")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
word_count = adwentures_of_tom_sawer_sentences[-1].count(" ")
print(f"\nВ останньому реченні {word_count} слова")
