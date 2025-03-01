# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випрaавити\доповнити.
"""
def multiplication_table(number):

    multiplier = 1

    while True:
        result = number * multiplier
        if result > 25:
            break
        print(f"Task 1 --> {number} x {multiplier} = {result}")

        multiplier += 1

multiplication_table(3)
print('.................................................................')
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_of_two(a,b):
    return a + b

print(f"Task 2 -->  {sum_of_two(1,2)}")
print('.................................................................')



# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def average(data):
    return sum(data) / len(data)

nums = [1, 2, 3, 4]
print(f"Task 3 --> {average(nums)}")   
print('.................................................................')



# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_string(data):
    return data[::-1]

print(f"Task 4 --> {reverse_string("Hello")}")
print('.................................................................')
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_in_list(words):
    return max(words, key=len)
wow = ["hello", "one", "two"]
print(f"Task 5 --> {longest_in_list(wow)}")
print('.................................................................')


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(f"Task 6 --> {find_substring(str1, str2)}") # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(f"Task 6 --> {find_substring(str1, str2)}") # поверне -1
print('.................................................................')

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# Task 7 
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
def list_of_squares(data):
    return [x**2 for x in data if x % 2 == 0]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Task 7 --> {list_of_squares(numbers)}")
print('.................................................................')

# Task 8
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""

def all_except_orange(data):
    result = []
    for x in data:
        if x == "orange":
            continue
        result.append(x)
    return result

fruits = ["apple", "banana", "orange", "grape", "mango"]
print(f"Task 8 --> {all_except_orange(fruits)}")
print('.................................................................')

# Task 9 
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""
def check_alien_color(data):
    if data == "green":
        return "Task 9 --> You just got 5 points"
    else:
        return "Wrong color"

print(f"Task 9 --> {check_alien_color("green")}")
print('.................................................................')

# Task 10 
""" Add all numbers from list all even numbers"""
def add_all_nums_from_list(lst):
    return sum(x for x in lst if x % 2 == 0)

lst3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Task 10 --> {add_all_nums_from_list(lst3)}")