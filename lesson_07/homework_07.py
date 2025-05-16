# Task 1: Табличка множення до добутку ≤ 25
def multiplication_table(number):
    """
    Друкує табличку множення для заданого числа до тих пір, поки добуток ≤ 25.
    """
    multiplier = 1
    while True:
        result = number * multiplier
        if result > 25:
            break
        print(f"{number}x{multiplier}={result}")
        multiplier += 1

# Task 2: Сума двох чисел
def add_numbers(a, b):
    """
    Повертає суму двох чисел.
    """
    return a + b

# Task 3: Середнє арифметичне списку
def average(numbers):
    """
    Повертає середнє арифметичне списку чисел.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Task 4: Рядок у зворотному порядку
def reverse_string(s):
    """
    Повертає рядок у зворотному порядку.
    """
    return s[::-1]

# Task 5: Найдовше слово у списку
def longest_word(words):
    """
    Повертає найдовше слово у списку слів.
    """
    if not words:
        return ""
    return max(words, key=len)

# Task 6: Індекс підрядка або -1
def find_substring(str1, str2):
    """
    Повертає індекс першого входження str2 у str1 або -1, якщо не знайдено.
    """
    return str1.find(str2)

# ======= Приклади використання =======

# Task 1
multiplication_table(3)
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15
# 3x6=18
# 3x7=21
# 3x8=24

# Task 2
print(add_numbers(5, 7))  # 12

# Task 3
print(average([1, 2, 3, 4, 5]))  # 3.0

# Task 4
print(reverse_string("hello"))  # "olleh"

# Task 5
print(longest_word(["cat", "elephant", "dog"]))  # "elephant"

# Task 6
print(find_substring("Hello, world!", "world"))  # 7
print(find_substring("The quick brown fox", "cat"))  # -1
