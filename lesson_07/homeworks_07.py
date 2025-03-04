# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
from typing import Sized


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number:
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1


multiplication_table(9)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def sum_a_and_b(a: int, b: int) -> int:
    result = a + b
    print(f"Сума двох чисел: {str(a)} + {str(b)} = {result}")
    return result


sum_a_and_b(3, 10)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def math_average(*args):
    result = sum(args) / len(args)
    print(f"Середнє арифмечне списку чисел {args} = {result}")
    return result


math_average(5, 10, 15)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reversed_string(string: str):
    result = string[::-1]
    print(f"Строка {string} навпаки стала: {result}")
    return result


reversed_string("Hello")
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def longest_word(words: list) -> str:
    result = max(words, key=len)
    print(f"Найдовше слово: {result}")
    return result


longest_word(["word", "tetiana", "1"])

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1: str, str2: str) -> int:
    result = str1.find(str2)
    if result == -1:
        print(f"Строка '{str2}' не входить в строку '{str1}'. Індекс = {result}")
    else:
        print(f"Індекс входження підстроки '{str2}' в строку '{str1}' = {result}")
    return result


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
'''alien color - функція, що приймає колір, і повертає результат в залежності, який колір було задано'''


def alien_color(color: str) -> str:
    if color == 'blue':
        print(f"Колір: {color}! гравець заробив 5 балів.")
        return "Зароблено 5 балів!"
    else:
        print(f"Error color.")
    return "Error color"


alien_color("blue")  # поверне Колір: blue! гравець заробив 5 балів.
alien_color("white")  # поверне Error color.

# task 8
'''get_even_squares - функція, що приймає список чисел, і повертає список квадратів парних чисел'''


def get_even_squares(numbers: list) -> list:
    result = [i ** 2 for i in numbers if i % 2 == 0]
    print(f"Квадрати парних чисел = {result}")
    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
get_even_squares(numbers)  # викликаємо функцію і передаємо в агрумент список чисел numbers

# task 9
'''Функція без аргументів, в собі містить ввод строки (назва піци) від користувача, доки не введено 'quit'.'''


def order_pizza():
    while True:
        pizza_topping = input("Введіть начинку для піци (для завершення замовлення введіть 'quit'): ").strip()

        if pizza_topping.lower() == 'quit':  # Перевіряємо без урахування регістру
            print("Дякуємо! Прийнято замовлення.")
            break
        elif pizza_topping == "":
            print("Будь ласка, введіть назву начинки.")
        else:
            print(f"Додамо {pizza_topping} до вашої піци.")


# викликаємо функцю
order_pizza()

# task 10
'''Функція замінює переноси рядків на пробіли у тексті.'''


def fix_text_format(text: str) -> str:
    result = text.replace("\n", " ")
    print(f"Оновленний текст: {result}")
    return result


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
."""

fix_text_format(adwentures_of_tom_sawer)  # викликаємо функцію для обробки тексту
