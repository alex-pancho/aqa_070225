# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number: (int, float)) -> None:
    # Initialize the appropriate variable
    multiplier = 1
    if number  <= 0:
        print("Введіть число більше 0")
    elif number > 25:
        print("Введіть число менше 25")
    else:
        while number * multiplier <= 25:
            result = number * multiplier
            if  result >= 25:
                break
            print(str(number) + "x" + str(multiplier) + "=" + str(result))
            # Increment the appropriate variable
            multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_two_numbers(a: int | float, b: int | float) -> int | float | str:
    if not all(isinstance(i, (int, float)) for i in (a, b)):
        return "Потрібно ввести числа"
    return a + b

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_of_list(lst: list[int | float]) -> int | float | str:
    if not lst:
        return "Пустий список"
    if not all(isinstance(i, (int, float)) for i in lst):
        return "Потрібно ввести список чисел"
    return sum(lst) / len(lst)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(string: str) -> str:
    if not isinstance(string, str):
        return "Потрібно ввести рядок"
    elif len(string) == 0:
        return "Потрібно ввести рядок довжиною більше 0"
    return string[::-1]

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(lst: list[str]) -> str | list[str]:
    if not lst:
        return "Пустий список"
    if not all(isinstance(i, str) for i in lst):
        return "Потрібно ввести список слів"
    max_length = max(map(len, lst))
    longest_word = [word for word in lst if len(word) == max_length]
    return longest_word if len(longest_word) > 1 else longest_word[0]

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1: str, str2: str) -> int | str:
    if not all(isinstance(i, str) for i in (str1, str2)):
        return "Потрібно ввести два рядки"
    if not str2:
        return "Потрібно ввести другий рядок довжиною більше 0"
    if str2 in str1:
        return str1.index(str2)
    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
"""Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
Строку отримати за допомогою функції input()"""
def count_unique_characters() -> bool:
    string = input("Введіть строку: ")
    if len(set(string)) > 10:
        print(True)
        return True
    else:
        print(False)
        return False

# task 8
"""Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" 
(враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "h"."""
def input_word_with_h() -> None:
    while True:
        word = input("Введіть слово, в якому є літера 'h': ")
        if "h" in word or "H" in word:
            break

# task 9
"""Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. 
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1. 
Данні в лісті можуть бути будь якими"""
def get_strings_from_list(lst: list) -> list:
    return [str(i) for i in lst if isinstance(i, str)]

# task 10
"""Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті"""
def sum_of_even_numbers(lst: list[int]) -> int:
    return sum(i for i in lst if i % 2 == 0)

