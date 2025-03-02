   # task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
print("Task 1\n")
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        
        # Помилка: порівняння числа зі строкою "25"
        if result > 25:
            break  # Виходимо з циклу, якщо добуток більше 25
        
        print(f"{number}x{multiplier}={result}")
        
        # Помилка: змінна "multi" не існує, потрібно "multiplier"
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

print("\n")

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
print("Task 2\n")
def sum_2_numbers (a, b):
    return a + b


a = 4
b = 5
result = sum_2_numbers (a, b)
print(result)
print("\n")


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print("Task 3\n")

def average_number_of_list (list_of_numbers):
    if len(list_of_numbers) == 0:
        return("Error. List is empty")
    else:
        average = sum(list_of_numbers) / len(list_of_numbers)
        return average

list = [1, 4, 5, 6, 10, 7, 8, 9, 3]
result = average_number_of_list(list)
print(f'Середнє арифметичне: {result:.2f}')

print("\n")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

print("Task 4\n")

def reverse_line (text):
    return text [::-1]


line = input('Подай рядок: \n')
result = reverse_line(line)
print('Рядок у зворотньому напрямку: ', result)

print("\n")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

print("Task 5\n")

def long_word(words):
    return max(words, key=len)


words = ["Kick", "Range", "BMW", "Czekolada"]
longest_word = long_word(words)
print("Надовше слово у списку: ", longest_word)

print("\n")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

print("Task 6\n")

def find_substring(str1, str2):
    return str1.find(str2)  # Використовуємо метод find(), який повертає індекс або -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

print("\n")

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
print("Task 7\n")

def reverse_words(sentence):
    """
    Приймає речення і повертає його, де всі слова записані у зворотному порядку.
    """
    return ' '.join(sentence.split()[::-1])

line = input("Подай речення: \n")

print("Речення у зворотньому напрямку: \n", reverse_words(line))

print("\n")

print("Task 8\n")

def count_vowels(text):
    """
    Підраховує кількість голосних у заданому тексті.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

print("Кількість голосних:", count_vowels("Hello, world!")) # 3

print("\n")

print("Task 9\n")

def filter_cars(car_data, search_criteria):
    """
    Фільтрує список автомобілів за заданими критеріями (рік >=, об'єм двигуна >=, ціна <=).
    Повертає список до 5 підходящих автомобілів, відсортованих за ціною за зростанням.
    """
    year_min, engine_min, price_max = search_criteria
    filtered_cars = [
        (name, details) for name, details in car_data.items()
        if details[1] >= year_min and details[2] >= engine_min and details[4] <= price_max
    ]
    filtered_cars.sort(key=lambda x: x[1][4])
    return filtered_cars[:5]

car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000)
}

search_criteria = (2017, 1.6, 36000)
print(filter_cars(car_data, search_criteria))

print("\n")

print("Task 10\n")

def swap_elements(lst, index1, index2):
    """
    Міняє місцями два елементи у списку lst за заданими індексами index1 та index2.
    Повертає змінений список.
    """
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst

people = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(swap_elements(people, 1, 3))
