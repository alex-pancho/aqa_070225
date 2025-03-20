# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""

alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")

# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""

alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

# task 3
# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""

alien_colors = ['green', 'yellow', 'red']

for alien_color in alien_colors:
    if alien_color == 'green':
        print("You just earned 5 points!")
    elif alien_color == 'yellow':
        print("You just earned 10 points!")
    elif alien_color == 'red':
        print("You just earned 15 points!")

# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""

pizza_topping = ''
while pizza_topping != 'quit':
    pizza_topping = input("Enter a pizza topping or 'quit' to stop: ")
    if pizza_topping != 'quit':
        print(f"Adding {pizza_topping} to your pizza.")

# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр натурального числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть натуральне число: 12345
Сума цифр числа 12345: 15
"""

number = input("Enter a natural number: ")
sum_digits = sum(int(digit) for digit in number)
print(f"Sum of the digits of the number {number}: {sum_digits}")

# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""

total_sum = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    total_sum += number
print(f"The total sum is: {total_sum}")

# task 8
"""  З використанням циклу for реалізуйте гру "Вгадай число".
Початок програми написаний, гравець має 5 спроб відгадати випадкове число від 1 до 20,
яке було згенеровано за допомогою функції randint() модуля random.
У кожній спробі гравець вводить своє припущення, після чого програма повідомляє, чи
було припущення занадто великим або занадто малим, чи гравець вгадав число.
"""
import random

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

# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""

fruits = ["apple", "banana", "orange", "grape", "mango"]
for fruit in fruits:
    if fruit == "orange":
        continue
    print(fruit)

# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [[x**2 for x in numbers if x % 2 == 0]]
print(result)  #  [4, 16, 36, 64, 100]

