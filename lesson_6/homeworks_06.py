# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""

alien_color = "green"

if alien_color == "green":
    print(f"Task 1 --> You just got 5 points")

print('.................................................................')

# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""

alien_color = "yellow"
if alien_color == "green":
    print(f"Task 2 --> You just got 5 points")
else:
    print(f"Task 2 --> You just got 10 points")

print('.................................................................')

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

for x in alien_color:
    if x == "red":
        print(f"Task 3/4 --> You just got 15 points")
    elif x == "yellow":
        print(f"Task 3/4 --> You just got 10 points")
    else:
        print(f"Task 3/4 --> You just got 5 points")

print('.................................................................')

# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""

pizza_topping = input('Task 5 --> Please enter pizza topping or \'quit\' to exit: ')


while pizza_topping != 'quit':
    print(f'Task 5 --> : {pizza_topping} is added')
    pizza_topping = input('Task 5 -->  Please provide additional pizza topping or \'quit\' to exit: ')

print('.................................................................')

# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр натурального числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть натуральне число: 12345
Сума цифр числа 12345: 15
"""

numbers = input("Task 6 --> Please provide your natural number: ")

if numbers.isdigit() and int(numbers) > 0:
    res = sum(int(x) for x in numbers)  
    print(f"Task 6 --> The sum of digits: {res}")
else:
    print("Task 6 --> Invalid input! Please enter a natural number.")

print('.................................................................')

# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""

total_sum = 0
while True:
    user_num = int(input("Task 7 --> Please provide your num and use 0 to stop : "))
    if user_num == 0:
        break
    total_sum += user_num

print(f"Task 7 --> The total sum is: {total_sum}")
print('.................................................................')

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

while guesses < max_guesses:
    user_guess = int(input("Task 8 --> Please provide your num : "))
    guesses += 1
    if user_guess == secret_number:
        print(f"Task 8 --> Congratulation you guessed secret number {secret_number} from {guesses} guesses ")
        break
    elif user_guess < secret_number:
        print("Task 8 --> Your guess is lower")
    else:
        print("Task 8 --> Your guess is higher")
    
    if guesses == max_guesses:
        print(f"Task 8 --> You have used all atempts, secret num was {secret_number}.")
print('.................................................................')

# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""

fruits = ["apple", "banana", "orange", "grape", "mango"]
for x in fruits:
    if x == "orange":
        continue
    print(f"Task 9 --> {x}")

print('.................................................................')

# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x**2 for x in numbers if x % 2 == 0]
print(f"Task 10 --> {result}")  #  [4, 16, 36, 64, 100]
