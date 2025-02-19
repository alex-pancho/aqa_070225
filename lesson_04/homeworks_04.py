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
print(f'Заміна абзацу на пробіл:\n{adwentures_of_tom_sawer}\n')

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(f'Заміна на пробіл:\n{adwentures_of_tom_sawer}\n')

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(f'Заміна не більше одного пробілу між словами:\n{adwentures_of_tom_sawer}\n')

# task 04 
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = adwentures_of_tom_sawer.count('h')
print("Літера 'h' зустрічається", count_h, "разів\n")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count_capital = 0
for word in adwentures_of_tom_sawer.split():
    if word[0].isupper():
        count_capital += 1
print(f"Кількість слів, що починаються з великої літери: {count_capital}\n")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

first_index = adwentures_of_tom_sawer.find('Tom')
second_index = adwentures_of_tom_sawer.find('Tom', first_index +1)
print(f"Cлово 'Tom' зустрічається вдруге  у тексті на позиції: {second_index}\n")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.replace(". ",".\n")
print('Розділена змінна adwentures_of_tom_sawer по кінцю речення:')
print(f'{adwentures_of_tom_sawer_sentences}\n')

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
sentences = adwentures_of_tom_sawer.split('. ') 
if len(sentences) > 3:  
    print(f"Четверте речення є:\n{sentences[3].lower()}\n")  
else:  
    print("Четвертого речення немає у тексті.")  

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith("By the time"):
        print("Є речення, що починається з 'By the time'!")
    
else:
    print(f"Немає речень, що починаються з 'By the time'.\n")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

if adwentures_of_tom_sawer_sentences:
    last_sentence = adwentures_of_tom_sawer_sentences[-1].strip()
    word_count = len(last_sentence.split())  
    print("Кількість слів в останньому реченні:", word_count)
else:
    print("Текст не містить речень.")
