# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 10:
        result = number * multiplier
        if result <= 25:
            print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # десь тут помилка, а може не одна
        elif result > 25:
            # Enter the action to take if the result is greater than 25
            break
        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

print('---------------------------------------------------------------------------------------------')

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_numbers(number_1:int, number_2:int) -> int:
    """Function sum two integers."""
    result_of_sum = number_1 + number_2
    return(result_of_sum)

number_1 = 189
number_2 = 568

print(f'TASK 2: The sum of two numbers {number_1} and {number_2} is: {sum_two_numbers(number_1, number_2)}')

print('---------------------------------------------------------------------------------------------')

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_number(number_list:list) -> float:
    """ Function returns the average number from the initial list.\n
    The result is a float rounded to 2 digits after the comma."""
    average_numbers_calc = round(sum(number_list)/len(number_list), 2)
    return(average_numbers_calc)

number_list = [4,6,7,9,9,5]

print(f'TASK 3: The average number of entered list {number_list} is: {average_number(number_list)}')

print('---------------------------------------------------------------------------------------------')

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(string:str) -> str:
    """Function returns a reversed string."""
    reversed_string = string[::-1]
    return(reversed_string)
    
string = 'Hello'

print(f'TASK 4: Reversed \'{string}\' string value is: \'{reverse_string(string)}\'')

print('---------------------------------------------------------------------------------------------')

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word_from_list (words_list:list) -> str:
    """Function returns the longest word from the list."""
    longest_word = max(words_list, key=len)
    return(longest_word)
    
words_list = ["apple", "banana", "onion", "cucumber", "bread"]

print(f'TASK 5: The longest word from the list {words_list} is: {longest_word_from_list(words_list)}')
    
print('---------------------------------------------------------------------------------------------')

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1:str, str2:str) -> int:
    """ Function checks if str1 contains str2.\n 
    Returns index (position) of the first occurrence of str2 in str1.\n
    Returns '-1' if str1 does not contain str2."""
    if str2 in str1:
        return(str1.index(str2))
    else:
        return(-1)

str1 = "Hello, world!"
str2 = "world"
print(f'TASK 6: Index of the first occurrence of str2 in str1 (-1 if str1 does not contain str2): {find_substring(str1, str2)}') # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(f'TASK 6: Index of the first occurrence of str2 in str1 (-1 if str1 does not contain str2): {find_substring(str1, str2)}') # поверне -1

print('---------------------------------------------------------------------------------------------')

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""

def calculator(number_input:int) -> int:
    """Function calculates the sum of entered natural numbers.\n
    To exit and show the sum of numbers enter '0'."""
    number_input = int(input('TASK 7: Please enter any natural number: '))
    sum_of_numbers = 0
    while number_input != 0:
        sum_of_numbers = sum_of_numbers + number_input
        number_input = int(input('TASK 7: Please enter any natural number that should be added or 0 to exit and show sum of numbers: '))
        if number_input == 0:
            return(sum_of_numbers)

print(f'TASK 7: The sum of entered numbers is: {calculator(0)}')

print('-----------------------------------------------------------------------------------')

# task 8
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
def pow_even_number_list(number_list:list) -> list:
    """Function returns list with power even numbers."""
    pow_number_list = [number**2 for number in number_list if number % 2 == 0]
    return(pow_number_list)

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'TASK 8: New list with pow even numbers: {pow_even_number_list(number_list)}')  #  [4, 16, 36, 64, 100]

print('---------------------------------------------------------------------------------------------')

# task 9

'''Рахування унікальних символів в строці
Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, 
інакше - False. Строку отримати за допомогою функції input()'''


def count_unique_characters(str_for_count:str) -> bool:
    """Functions count unique characters in string and:\n
    - returns 'True' if string contains more than 10 unique characters;\n
    - returns 'False' if string contains less than 10 unique characters.
    """
    set_for_count = set(str_for_count)
    set_len = len(set_for_count)
    if set_len > 10:
        return(True)
    if set_len <= 10:
        return(False)

str_for_count = 'qwertttttttttttyyyyyyyyyy'

print(f'TASK 9: String contains more than 10 unique characters? Response: {count_unique_characters(str_for_count)}')

print('---------------------------------------------------------------------------------------------')

# task 10
"""  Напишіть програму, яка знаходить суму всіх цифр натурального числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть натуральне число: 12345
Сума цифр числа 12345: 15
"""

def sum_of_numbers(number:int) -> int:
    """Function returns the sum of all digits of the entered integer."""
    number_string = str(number)
    numbers_sum = 0
    for number in number_string:
        numbers_sum = numbers_sum + int(number)
    return(numbers_sum)

number = 12345

print(f'TASK 10: The sum of all numbers is: {sum_of_numbers(number)}')

print('---------------------------------------------------------------------------------------------')
