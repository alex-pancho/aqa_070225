# task 1
"""  Функція, яка обчислює суму двох чисел.
"""
def add_numbers(a, b):
    if not isinstance(a,(int, float)) or not isinstance(b, (int, float)):
       raise TypeError("Both arguments must be numbers")
    return a + b



# task 2
"""  Функція, яка розрахує середнє арифметичне списку чисел.
"""
def new_average(small_list):
    if len (small_list) == 0:
      raise ValueError("Error: List is empty")
    return sum(small_list) / len(small_list)

# task 3
"""  Функція, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(text):
    if not isinstance(text, str):
       raise TypeError("Input must be a string")
    return text [::-1]



# task 4
"""  Функція, яка приймає список слів та повертає найдовше слово у списку.
"""
def long_word(words):
    if not words:
       raise ValueError("List is empty")
    return max(words, key=len)



# task 5
"""  Функція, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
  if not str2:
     raise ValueError("Substring cannot be empty")
  return str1.find(str2)

