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
print(f'''Текст із заміненим кінцем абзацу на пробіл: 
{adwentures_of_tom_sawer}''')

print('-----------------------------------------')

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("...."," ")
print(f'''Текст із заміненим '....' на пробіл: 
{adwentures_of_tom_sawer}''')

print('-----------------------------------------')

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer)
print(f'''Текст у якому не більше одного пробілу між словами:       
{adwentures_of_tom_sawer}''')

print('-----------------------------------------')

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h_letter = adwentures_of_tom_sawer.count('h')
print(f'Літера "h" зустрічається у тексті {count_h_letter} разів.')

print('-----------------------------------------')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

count_words_from_upper_letter =  adwentures_of_tom_sawer.count('A') + adwentures_of_tom_sawer.count('B') \
+ adwentures_of_tom_sawer.count('C') + adwentures_of_tom_sawer.count('D') + adwentures_of_tom_sawer.count('E') \
+ adwentures_of_tom_sawer.count('F') + adwentures_of_tom_sawer.count('G') + adwentures_of_tom_sawer.count('H') \
+ adwentures_of_tom_sawer.count('I') + adwentures_of_tom_sawer.count('J') + adwentures_of_tom_sawer.count('K') \
+ adwentures_of_tom_sawer.count('L') + adwentures_of_tom_sawer.count('M') + adwentures_of_tom_sawer.count('N') \
+ adwentures_of_tom_sawer.count('O') + adwentures_of_tom_sawer.count('P') + adwentures_of_tom_sawer.count('Q') \
+ adwentures_of_tom_sawer.count('R') + adwentures_of_tom_sawer.count('S') + adwentures_of_tom_sawer.count('T') \
+ adwentures_of_tom_sawer.count('U') + adwentures_of_tom_sawer.count('V') + adwentures_of_tom_sawer.count('W') \
+ adwentures_of_tom_sawer.count('X') + adwentures_of_tom_sawer.count('Y') + adwentures_of_tom_sawer.count('Z')

print(f'З великої літери у тексті починається {count_words_from_upper_letter} слів.')

print('-----------------------------------------')

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
index_of_first_tom = adwentures_of_tom_sawer.find("Tom")
index_of_second_tom = adwentures_of_tom_sawer.find("Tom", index_of_first_tom + 1)

print(f'Слово Tom зустрічається вдруге на позиції: {index_of_second_tom}.')

print('-----------------------------------------')

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('.')
adwentures_of_tom_sawer_sentences = "\n".join(adwentures_of_tom_sawer_sentences)

print(f'''Розділена змінна adwentures_of_tom_sawer по кінцю речення (по крапці): 
{adwentures_of_tom_sawer_sentences}''')

print('-----------------------------------------')

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence = adwentures_of_tom_sawer_sentences[407:644].lower()
print(f'''Виведений четвертий рядок у нижньому регістрі: 
{fourth_sentence}''')

print('-----------------------------------------')

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
# Виведено окремо кожне речення по індексах

first_sentence = adwentures_of_tom_sawer_sentences[0:75]
second_sentence = adwentures_of_tom_sawer_sentences[75:289].strip()
third_sentence = adwentures_of_tom_sawer_sentences[289:407].strip()
fourth_sentence = adwentures_of_tom_sawer_sentences[407:644].strip()
fifth_sentence = adwentures_of_tom_sawer_sentences[644:786].strip()

# Перевіряємо чи кожне речення починається з "By the time"

first_sentence_start_check = first_sentence.startswith("By the time")
# Окрема перевірка першого речення
# print(f'Чи починається перше речення з \'By the time\'? Відповідь: {first_sentence_start_check}')

second_sentence_start_check = second_sentence.startswith("By the time")
# Окрема перевірка другого речення
# print(f'Чи починається друге речення з \'By the time\'? Відповідь: {second_sentence_start_check}')

third_sentence_start_check = third_sentence.startswith("By the time")
# Окрема перевірка третього речення
# print(f'Чи починається третє речення з \'By the time\'? Відповідь: {third_sentence_start_check}')

fourth_sentence_start_check = fourth_sentence.startswith("By the time")
# Окрема перевірка чнтвертого речення
# print(f'Чи починається четверте речення з \'By the time\'? Відповідь: {fourth_sentence_start_check}')

fifth_sentence_start_check = fifth_sentence.startswith("By the time")
# Окрема перевірка п'ятого речення
# print(f'Чи починається п'яте речення з \'By the time\'? Відповідь: {fifth_sentence_start_check}')

# Перевіряємо чи якесь речення починається з "By the time"

any_sentence_start_check = first_sentence_start_check or second_sentence_start_check or third_sentence_start_check or fourth_sentence_start_check or fifth_sentence_start_check
print(f'Чи починається якесь речення з \'By the time\'? Відповідь: {any_sentence_start_check}')

print('-----------------------------------------')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
fifth_sentence_list = fifth_sentence.split()
fifth_sentence_list_len = len(fifth_sentence_list)
print(f'Кількість слів останнього речення з змінної \'adwentures_of_tom_sawer_sentences\': {fifth_sentence_list_len}.')

print('-----------------------------------------')
