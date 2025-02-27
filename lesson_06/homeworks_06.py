# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""
game_color = input('Welcome. Guess the collor of the alien:''\n')
alien_color = 'green'
if game_color == alien_color:
    print('# task 1: Perfect! You earned 5 points:') 
else:
    print('# task 1: Don\'t give up. Try again!')

# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""
game_color = input('Welcome again. Guess the collor of alien:''\n')
alien_color = 'green'
if game_color == alien_color:
    print('# task 2: Great! You just earned 5 points.') 
else:
    print('# task 2: Great! You just earned 10 points')
# task 3
# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""

alien_color = ['green', 'yellow', 'red']
for color in alien_color:
    if color == 'green':
        print('# task 3, 4: Good job. You just earned 5 points!') 
    elif color == 'red':
        print('# task 3, 4: Good job. You just earned 15 points!')
    else:
        print('# task 3, 4: Good job. You just earned 10 points!')

# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
while True:
    pizza_topping = input("Please enter a topping for your pizza (type 'quit' to stop):"'\n')
    if pizza_topping == 'quit':
       print("task 5: Great choice. Thanks for building your pizza!")
       break
    print(f"task 5: {pizza_topping} has been added to your pizza.")

# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр натурального числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть натуральне число: 12345
Сума цифр числа 12345: 15
"""
numbers = (input('Enter a natural numbers: \n'))
sum_of_digits = 0
for digit in numbers:
    sum_of_digits += int(digit)
print(f"task 6: The sum of the digits of the numbers {numbers}: is  {sum_of_digits} ")

# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""
sum_of_number = 0
while True:
    numbers = input('Please, Enter a number:\n')
    if numbers == '0':
        break
    sum_of_number += int(numbers)
print(f'task 7: Total sum of entered numbers: {sum_of_number}')

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
print("Guess the number between 1 and 20 in 5 attempts!")

for attempt in range(1, max_guesses + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))  
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"task 8: Congratulations! You guessed the number {secret_number} in {attempt} attempts!")
        break  
else:  
        print(f"task 8: You didn't guess the number. The correct number was {secret_number}.")

# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]
for i in fruits:
     if i == 'orange':
          continue
     else: 
          print(f'task 9: {i}')

# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x **2 for x in numbers if x % 2 == 0]
print(f'task 10: {result}')  #  [4, 16, 36, 64, 100]
