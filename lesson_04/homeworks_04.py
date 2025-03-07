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
words = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = " ".join(words)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
h_count = adwentures_of_tom_sawer.count("h")
print(h_count)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words = adwentures_of_tom_sawer.split()
count = 0
for word in words:
    if word[0].isupper():
        count = count + 1
print(count)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first = adwentures_of_tom_sawer.find("Tom")
second = adwentures_of_tom_sawer.find("Tom", first + 1)
print(second)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")
for i in range(len(adwentures_of_tom_sawer_sentences) - 1):
    adwentures_of_tom_sawer_sentences[i] = adwentures_of_tom_sawer_sentences[i] + "."

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth = adwentures_of_tom_sawer_sentences[3]
fourth_lower = fourth.lower()
print(fourth_lower)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
found = False
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        found = True
print(found)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1]
word_count = len(last_sentence.split())
print(word_count)