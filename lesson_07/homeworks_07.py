def print_task(task_number):
    print(f"\n\n---Task {task_number}---\n")

# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
print_task(1)


def multiplication_table(number): 
    if not isinstance(number, int):
        print("Для вводу доступні тільки цілі числа!") 
        return 
    if number <= 0:
        print("Значення повинно бути більше нуля!")
        return
    multiplier = 1   
    while True:
        result = number * multiplier
        if result > 25:
            break
        print(f"{number} x {multiplier} = {result}")
        multiplier += 1


multiplication_table(5)


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
print_task(2)


def sum_pair(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return "Для вводу доступні тільки числа!"
    return a + b


sum_result = sum_pair(11, 5)
print(sum_result)


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print_task(3)


def avr_sum(numbers):
    if not numbers:  
        return "Список пустий. Введіть числа!"
    for num in numbers:
        if not isinstance(num, (int, float)):
            return "Для вводу доступні тільки числа!"
    return sum(numbers) / len(numbers)


avr_result = avr_sum([1, 2, 4, -5])
print(avr_result)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print_task(4)


def reverse(string):
    if not isinstance(string, str):
        return "Введіть коректний рядок!"
    return string[::-1]     


result_reverse = reverse("BOB LOL HOH NAN")
print(result_reverse)
    

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print_task(5)


def longest_word(words):
    if not words:
        return "Список не може бути порожнім. Введіть слова!"
    for word in words:
        if not isinstance(word, str): 
            return "Для вводу доступні тільки слова"
    return max(words, key=len)


result_words = longest_word(["One", "Two", "Three", "Four", "Five"])
print(result_words)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

print_task(6)


def find_substring(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        return "Для вводу доступні тільки слова!"
    return str1.find(str2)

        
str1 = "Hello,world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""

print_task(10)


def sum_two_numbers(a, b):
    """
    Обчислює суму двох чисел. 
       
    :param a: Перше число.
    :param b: Друге число.
    :return: Сума двох чисел або повідомлення про помилку.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Для вводу доступні тільки числа!"
    return a + b


print(sum_two_numbers(1, 3))


def sum_of_digits(number: int) -> int:
    """
    Функція обчислює суму всіх цифр натурального числа.
    
    :params number: Натуральне число, для якого потрібно обчислити суму цифр
    :return: Сума цифр числа
    """
    sum_digits = 0
    for digit in str(number):
        sum_digits += int(digit)
    return sum_digits


print(sum_of_digits(445))


def swap_dict_keys_and_values(input_dict):
    """
    Функція міняє місцями ключі та значения словника.

    :param input_dict: Словник
    :return: Новий словник з поміняними місцями ключами та значенями
    """
    return {value: key for key, value in input_dict.items()}


original_dict = {"Key_Key": "Key_Value", "Value_Key": "Value_Value"}
swapped_dict = swap_dict_keys_and_values(original_dict)
print(swapped_dict)


def clean_string(input_string):
    """
    Функція видяляє зайві пробіли та залишає тільки один пробіл між словами.

    :param input_string: Вхідна строка
    :return: Строка без зайвих пробілів
    """
    return " ".join(input_string.split())


dirty_string = "  Hello     world!  Привіт    Свіііт!. "
cleaned_string = clean_string(dirty_string)
print(cleaned_string)
