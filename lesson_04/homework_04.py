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
print(f"task 01. Заміна кінця абзацу на пробіл.\n   Змінений текст: {adwentures_of_tom_sawer}")

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(f"task 02. Заміна .... на пробіл.\n   Змінений текст: {adwentures_of_tom_sawer}")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(f"task 03. Заміна більше одного пробілу на один.\n    Змінений текст: {adwentures_of_tom_sawer}")

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = adwentures_of_tom_sawer.count("h")
print(f"task 04. Кількість літер 'h' у тексті: {count_h}")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count_title_words = len([word for word in adwentures_of_tom_sawer.split() if word.istitle()])
print(f"task 05. Кількість слів, що починаються з великої літери: {count_title_words}")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
position_tom = adwentures_of_tom_sawer.find("Tom", adwentures_of_tom_sawer.find("Tom") + 1)
print(f"task 06. Позиція другого слова 'Tom': {position_tom}")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = [sentence.strip() for sentence in adwentures_of_tom_sawer.split(".")
                                     if sentence.strip()]
print(f"task 07. Розділений текст по реченнях: {adwentures_of_tom_sawer_sentences}")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
adwentures_of_tom_sawer_sentences_4 = adwentures_of_tom_sawer_sentences[3].lower()
print(f"task 08. Четверте речення в нижньому регістрі: {adwentures_of_tom_sawer_sentences_4}")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
find_sentence = [sentence for sentence in adwentures_of_tom_sawer_sentences
                 if sentence.strip().startswith("By the time")]
print(f"task 09. Чи починається яке-небудь речення з 'By the time': {find_sentence}")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
count_words_last_sentence = len(adwentures_of_tom_sawer_sentences[-1].split())
print(f"task 10. Кількість слів останнього речення: {count_words_last_sentence}")
