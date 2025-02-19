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
print(f"Task 1 --> {adwentures_of_tom_sawer}")

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(f"Task 2 --> {adwentures_of_tom_sawer}")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(f"Task 3 --> {adwentures_of_tom_sawer}")

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
counted = adwentures_of_tom_sawer.count("h")
print(f"Task 4 --> {counted} times letter h in text")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count_capitalized = sum(word[0].isupper() for word in adwentures_of_tom_sawer.split())
print(f"Task 5 --> {count_capitalized} times words start with capitaliezed")
# task 06
"""Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

first_index = adwentures_of_tom_sawer.find("Tom")
second_index = adwentures_of_tom_sawer.find("Tom", first_index+1)
print(f"Task 6 --> Second time we can find 'Tom' on {second_index} index")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")
print(f"Task 7 --> {adwentures_of_tom_sawer_sentences}")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(f"Task 08 --> {adwentures_of_tom_sawer_sentences[3]}")
lower_4th = adwentures_of_tom_sawer_sentences[3].lower()
print(f"Task 8 --> {lower_4th}")


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for x in adwentures_of_tom_sawer_sentences:
    if x.startswith("By the time"):
        print(f"Task 09 --> {True}")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
counted_last = len(adwentures_of_tom_sawer_sentences[-1].split())
print(f"Task 10 --> Amount of words in last sentence is {counted_last}")