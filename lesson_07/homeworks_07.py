# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True: #multiplier <= number:
        result = number * multiplier
        # десь тут помилка, а може не одна
        if  result >= 25:
            # Enter the action to take if the result is greater than 25
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
def summa(a, b):
    return a + b
print("Task 3 - returned sum of a + b = ", summa(2,3))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
numbers = [1, 2, 3]
def arithmetic_mean(array:list):
    """ Doc string """
    return sum(array) / len(array)
print("Task 4 - ", arithmetic_mean(numbers))
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reversed_string (text):
    return text[::-1]
print("Task 4 - reverted text: ", reversed_string("This is text to revert"))
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
list_of_words = ['apple', 'banana', 'cherry']
def longest_words(words):
    return max(words, key=len)
print("Task 5 - the longest word in the list: ", longest_words(list_of_words))
    
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print("task - 6 *********")
def find_substring(str1, str2):
     return str1.find(str2)
    #return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7   
def max_value(add_dict):
    """Знаходить ключ з максимальним значенням у словнику    add_dict"""
    return add_dict
print("Task 7 - ", max_value({"a":1, "b":2, "c":2, "d":3, 'size': 12}))


# task 8
def sum_dict(base_dict, add_dict):
    """Об"єднує два словника base_dict та add_dict  в новий словник sum_dict.
    Ключі, які збігаються, перетворються в строку та об'єднаються"""
    sum_dict = {}
    for key, value in base_dict.items():
        sum_dict[key] = value
    for key, value in add_dict.items():
        if key in sum_dict:
            sum_dict[key] = str(sum_dict[key]) + ", " + str(value)
        else:
            sum_dict[key] = value
    print("Combined base_dict and add_dict: ", sum_dict)
    return sum_dict

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
sum_dict(base_dict, add_dict)
# task 9
def guess_word(word = input("Введіть слово, яке містить літеру 'h'.")):
    """
    Просить ввести слова, поки не буде введено "h" (враховуються як великі так і маленькі).
    """
    while True:
        
        if "h" in word:
            print("Ви ввели праавильно слово", word)
            break
        else:
            print("Помилка! Слово не містить літери 'h'. Спробуйте ще раз.")
    
# task 10
def log_symetric_difference(set_1, set_2):
    """
    Знаходить суму елементів двох множин, які не є спільним.  
    """
    return print("The sum of different elements in set_1 and set_2: ", sum(set_1.symmetric_difference(set_2)))

log_symetric_difference({1, 2, 3, 4, 5}, {4, 6, 5, 10})

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""