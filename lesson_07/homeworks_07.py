# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True: 
        result = number * multiplier
        # десь тут помилка, а може не одна
        if  result > 25: 
            break
            # # Enter the action to take if the result is greater than 25
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
def add_numbers(a, b):
    return a + b

result = add_numbers(20, 30)
print(result)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def mean(a1, b1, c1):
    for i in str(mean):
        return (a1 + b1 + c1) // 3
result1 = mean(10, 20, 30)
print(result1)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse(task_4):
    return task_4[::-1]
result = reverse ("Написати функцію, яка приймає рядок та повертає його у зворотному порядку")
print(result)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest(fruits):
    max_word = fruits[0] 
    for i in fruits: 
        if len(i) > len(max_word):
            max_word = i 
    return max_word 

fruits = ['apple', 'banana', 'cucumber']
result2 = longest(fruits) 
print(result2)



# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
"""
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""


def alien_color_func()-> str: 
    """Перевіряє колір інопланетянина та повертає результат.

    :param alien_color: Колір інопланетянина
    :ptint: Результат гри
    """  
    alien_color = input("Якого кольору інопланетянин? ")
    if alien_color == "green":
        print("Так, ви щойно заробили 5 балів!") 
    elif alien_color == "red": 
        print("Ви програли:(")
    else: 
        print("Ви програли:(")
    
alien_color_func()
# task 8
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""
def alien_color_f()-> str:
    """Перевіряє колір інопланетянина та повертає результат.

    :param alien_color: Колір інопланетянина
    :print: Результат гри"""
    alien_color = input("Якого кольору інопланетянин? ")
    if alien_color == "green":
        print("Так, ви щойно заробили 5 балів!") 
    else:
        print("Ви, щойно заробили 10 балів:)")
alien_color_f()

# # task 9

"""напишіть цикл for що перебере і обробить всі значення списку alien_color
"""
def alien_color_task9 ()-> str:
    """Перевіряє колір інопланетянина та повертає результат.

    :param alien_color: Колір інопланетянина
    :print: Результат гри"""
    alien_color = ["green", "yellow", "red"]
    for i in alien_color:
        if i == "green":
            print("Так, ви щойно заробили 5 балів!") 
        elif i != "green" and i != "red":  # elif i == "yellow":
            print("Так, ви щойно заробили 10 балів!") 
        elif i == "red":
            print("Так, ви щойно заробили 15 балів!")
alien_color_task9()

# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
def pizza_topping_func()-> str:
    """Цикл, який пропонує користувачеві ввести ряд начинок
    для піци, доки він не введе значення 'quit'.
    :pizza_topping: це створення списку 
    :param topping: це текст який прохає ввести начинку
    :break: зупинка циклу після введення "quit"
    :param append(topping): додавання інших начинок до списку
    :print: Результат гри"""
    pizza_topping = []
    while True:
        topping = input("Які начинки ти хочеш? (напишіть 'quit' для виходу): ")
        if topping == "quit":
            print("Ви вийшли зі списку")  
            break
        pizza_topping.append(topping)
    print(pizza_topping)
pizza_topping_func()