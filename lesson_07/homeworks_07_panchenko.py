# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1
    while multiplier <= 10:  
        result = number * multiplier
        if result > 25:  
            break  
        print(f"{number} x {multiplier} = {result}")
        multiplier += 1

multiplication_table(3)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_of_two_numbers(a, b):
    return a + b

result = sum_of_two_numbers(4, 7)
print(result)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def average_of_list(numbers):
    if len(numbers) == 0:
        return 0 
    return sum(numbers) / len(numbers)

numbers = [5, 10, 15]
average = average_of_list(numbers)
print(average) 

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_string(input_string):
    return input_string[::-1]

reversed_str = reverse_string("hello")
print(reversed_str)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word(words):
    if not words: 
        return None
    return max(words, key=len)

words = ["apple", "banana", "grape"]
longest = longest_word(words)
print(longest)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))

def find_substring(str1, str2):
    return str1.find(str2)

print(find_substring("Hello, world!", "world"))
print(find_substring("The quick brown fox jumps over the lazy dog", "cat"))

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""

#7
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

print(sum_of_digits(12345))

#8
import random

def guess_the_number():
    secret_number = random.randint(1, 20)
    guesses = 0
    max_guesses = 5
    print("Guess the number between 1 and 20. You have 5 attempts!")

    while guesses < max_guesses:
        guess = int(input("Enter your guess: "))
        guesses += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number!")
            break
    else:
        print(f"Sorry, you've used all your attempts. The number was {secret_number}.")

#9
def skip_orange(fruits):

    for fruit in fruits:
        if fruit == "orange":
            continue
        print(fruit)


skip_orange(["apple", "banana", "orange", "grape", "mango"])

#10
def even_number_squares(numbers):
    return [x**2 for x in numbers if x % 2 == 0]

print(even_number_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))