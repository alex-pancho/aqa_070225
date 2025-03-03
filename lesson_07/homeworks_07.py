# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
print("\n Task 1")
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помилка, а може не одна
        if  result > 25:
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
print("\n Task 2")
def sum_of_numbers (num1, num2):
    """Oбчислює суму двох чисел"""
    print(num1+num2)

#print(sum_of_numbers(1, 2))
sum_of_numbers(1, 2)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print("\n Task 3")
def average_of_list (list_of_numbers):
    """Oбчислює середнє арифметичне списку чисел"""
    return round(((sum(list_of_numbers)/len(list_of_numbers))), 3)

print(average_of_list([5, 6, 1]))
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print("\n Task 4")
def reverse_string (string):
    "Повертає рядок у зворотному порядку"
    #Призначаємо індекс з якого будемо починати перезаписувати стрічку
    index = -1
    #Створюємо порожню стрічну, щоб записати в неї результат
    new_string = ""
    #Виконуємо цикл з останнтого елемента до першого
    while index >= -len(string):
        new_string += string[index]
        # Вибираємо наступний індекс у зворотньому напрямку
        index -= 1
    return new_string
print(reverse_string("12345"))    

def reverse_string2 (string):
    "Повертає рядок у зворотному порядку"
    return string[::-1]
print(reverse_string2("abcde"))    

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print("\n Task 5")
def longest_word (list_of_words):
    "Повертає перше найдовше слово у списку"

    #Позначаємо перше слово як найдовше
    long_word = list_of_words[0]
    #Виконуємо умови циклу
    for word in list_of_words:
        if len(word)> len(long_word):
            long_word = word
    return long_word
print(longest_word(["test", "one","test1","cat"]))
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print("\n Task 6")
def find_substring(str1, str2):
    "Повертає індекс першого входження другого рядка у перший рядок"
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
print("\n Task 7")
def unique_char(string:str):
    "Підраховує кількість унікальних символів в стрічці"
    #Кількість унікальних символів присвоюємо ноль
    unique_char_count = 0
    #Виконуємо умови циклу
    for char in string:
        if string.count(char) == 1:
            unique_char_count += 1
    return unique_char_count

print(unique_char("кількість унікальних символів в стрічці"))
# task 8
print("\n Task 8")
def sum_of_even_numbers(numbers_list: list):
    "Підраховує сумму усіх ПАРНИХ чисел в лісті"
    return sum (num for num in numbers_list if num % 2 == 0)
print(sum_of_even_numbers([1, 3, 5, 4, 8, 1, 9, -6]))

# task 9
print("\n Task 9")
def sum_of_digits(number: int):
    "Підраховує суму всіх цифр натурального числа"
    #Cуму цифр приймаємо ноль
    sum = 0
    #Виконуємо умови циклу
    for n in str(number):
        sum +=int(n) 
    return sum

print(sum_of_digits(2223))
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""
print("\n Task 10")
def square_of_even_numbers(given_list: list):
    "Підраховує та повертає список квадратів парних чисел зі заданого списку"
    return [num**2 for num in given_list if num % 2 ==0]
print(square_of_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  