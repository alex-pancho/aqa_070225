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

print("\n Task 01")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print (adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
print("\n Task 02")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print (adwentures_of_tom_sawer)


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print("\n Task 03")
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print (adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("\n Task 04")
adwentures_of_tom_sawer_count_h = adwentures_of_tom_sawer.count("h")
print(f'Літера "h" зустрічається у тексті {adwentures_of_tom_sawer_count_h} разів')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("\n Task 05")
words_starts_with_capital_letter_count = 0
words = adwentures_of_tom_sawer.split()
for i in words:
    if i[0].isupper() == True:
        words_starts_with_capital_letter_count += 1
print(f" У тексті {words_starts_with_capital_letter_count} слів починається з Великої літери")


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("\n Task 06")
print(f"Позиція, на якій слово Tom зустрічається вдруге - "
      f"{adwentures_of_tom_sawer.find("Tom", ((adwentures_of_tom_sawer.find("Tom")) +1))}")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

print("\n Task 07")
import re
adwentures_of_tom_sawer_sentences = re.split(r'[.!?]\s+', adwentures_of_tom_sawer)
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("\n Task 08")
print(str(adwentures_of_tom_sawer_sentences[3]).lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("\n Task 09")
bye_the_time=False
for i in range(len(adwentures_of_tom_sawer_sentences)):
    if str(adwentures_of_tom_sawer_sentences[i]).startswith("By the time") == True:
        bye_the_time=True
        break
    else:
        i += 1
if bye_the_time == True:
    print('Так, у тексті є речення, яке починається з "By the time"')
else:
     print('Ні, у тексті немає речення, яке починається з "By the time"')     


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("\n Task 10")
print(f"Кількість слів останнього речення - {len(adwentures_of_tom_sawer_sentences[-1].split())}")