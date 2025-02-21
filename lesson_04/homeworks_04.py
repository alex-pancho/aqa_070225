def print_task(task_number):
    print(f"\n\n---Task {task_number}---\n")


adventures_of_tom_sawer = """\
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
print_task(1)
indent_adventures_of_tom_sawer = adventures_of_tom_sawer.replace("\n", " ")
print(indent_adventures_of_tom_sawer)


# task 02 ==
""" Замініть .... на пробіл
"""
print_task(2)
dots_adventures_of_tom_sawer = indent_adventures_of_tom_sawer.replace("....", " ")
print(dots_adventures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print_task(3)
clean_sawer = dots_adventures_of_tom_sawer.replace("  ", " ").replace("  ", " ")
print(clean_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print_task(4)
h_word = clean_sawer.count("h")
print(h_word)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print_task(5)
count_upper = sum(clean_sawer.count(letter) for letter in "ABCDEFGHIJKLMNOPQRSTVUWXYZ")
print(count_upper)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print_task(6)
tom_pos = clean_sawer.find("Tom")
tom_pos2 = clean_sawer.find("Tom", tom_pos + 1)
print(tom_pos2)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print_task(7)
adventures_of_tom_sawer_sentences = clean_sawer.split(". ")
print(adventures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print_task(8)
sent_4 = adventures_of_tom_sawer_sentences[3].lower()
print(sent_4)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print_task(9)
search_text = ". By the time"
sent_present = f"Так, є речення яке починається з '{search_text}'"
sent_miss = f"Немає речень які починаються з '{search_text}'"
by_the = sent_present if search_text in clean_sawer else sent_miss
print(by_the)


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print_task(10)
last_sent = adventures_of_tom_sawer_sentences[-1]
word_split = last_sent.split()
word_len = len(word_split)
print(word_len)
