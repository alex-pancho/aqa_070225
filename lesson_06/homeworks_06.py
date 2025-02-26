# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""
print('-----------------------------------------------------------------------------------')

alien_color = 'green'

if alien_color == 'green':
    print('TASK 1: Congratulations! You just earned 5 points in game!')

print('-----------------------------------------------------------------------------------')

# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""
alien_color = 'red'

if alien_color == 'green':
    print('TASK 2: Congratulations! You just earned 5 points in game!')
else:
    print('TASK 2: Congratulations! You just earned 10 points in game!')

print('-----------------------------------------------------------------------------------')

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
    if alien_color == 'green':
        print('TASK 3,4: Congratulations! You just earned 5 points in game!')
    elif alien_color == 'red':
        print('TASK 3,4: Congratulations! You just earned 15 points in game!')
    else:
        print('TASK 3,4: Congratulations! You just earned 10 points in game!')

print('-----------------------------------------------------------------------------------')

# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
pizza_topping = input('TASK 5: Please enter pizza topping or \'quit\' to exit: ')

while pizza_topping != 'quit':
    print(f'TASK 5: {pizza_topping} is added')
    pizza_topping = input('TASK 5: Please enter additional pizza topping or \'quit\' to exit: ')

print('-----------------------------------------------------------------------------------')

# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр натурального числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть натуральне число: 12345
Сума цифр числа 12345: 15
"""

number_input = input('TASK 6: Please enter any natural number that should be summed: ')

sum_of_numbers = 0

if number_input.isdigit() == False:
    print('Incorrect input! Natural number required.')
else:
    for number in number_input:
        sum_of_numbers = sum_of_numbers + int(number)
    print(f'TASK 6: The sum of all numbers for {number_input} is: {sum_of_numbers}')

print('-----------------------------------------------------------------------------------')

# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""
number_input = int(input('TASK 7: Please enter any natural number: '))

sum_of_numbers = 0

while number_input != 0:
    sum_of_numbers = sum_of_numbers + number_input
    number_input = int(input('TASK 7: Please enter any natural number that should be added or 0 to exit and show sum of numbers: '))
    if number_input == 0:
        print(f'TASK 7: The sum of entered numbers is: {sum_of_numbers}')
        break

print('-----------------------------------------------------------------------------------')

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
print("Вгадайте число від 1 до 20 за 5 спроб!")


for quesses in range(max_guesses):
    number_from_user = int(input('TASK 8: Guess the secret number from 1 to 20: '))
    if secret_number > number_from_user:
        print('TASK 8: Secret number is greater!')
    elif secret_number < number_from_user:
        print('TASK 8: Secret number is less!')
    elif secret_number == number_from_user:
        print('TASK 8: Congratulations!!! You guessed secret number!')
        break
    guesses =+1

print('-----------------------------------------------------------------------------------')

# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]

for fruit in fruits:
    if fruit == 'orange':
        continue
    print(f'TASK 9: Fruit from list: {fruit}')

print('-----------------------------------------------------------------------------------')

# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [number**2 for number in numbers if number % 2 == 0]
print(f'TASK 10: New list with numbers: {result}')  #  [4, 16, 36, 64, 100]

print('-----------------------------------------------------------------------------------')
