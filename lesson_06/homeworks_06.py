def print_task(task_number):
    print(f"\n\n---Task {task_number}---\n")

# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""
print_task(1)

alien_color = ["green", "yellow", "red"]
if "green" in alien_color:
    print("Гравець щойно заробив 5 балів")

# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""
print_task(2)

alien_color = "yellow"
if alien_color == "green":
    print("Гравець щойно заробив 5 балів")
else:
    print("Гравець щойно заробив 10 балів")

# task 3
# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""

print_task(3)
print_task(4)

alien_color = ["green", "yellow", "red"]
for color in alien_color:
    if color == "green":
        print("Гравець щойно заробив 5 балів")
    elif color == "yellow":
        print("Гравець щойно заробив 10 балів")
    elif color == "red":
        print("Гравець заробив 15 очок")


# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
print_task(5)

pizza_topping = []
while True:
    topping = input("Яку начинку додати?\nДля закiнчення введiть 'quit'\n")
    if topping.lower() == "quit":
        print("Замовлення закiнчено")
        break     
    if topping.strip() == "":
        print("Ви не ввели начинку.")
        continue  
    pizza_topping.append(topping.title())
    print(f"{topping.title()} буде додано до пiци\n")

print(f"Доданi начинки: {', '.join(pizza_topping)}")

# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр натурального числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть натуральне число: 12345
Сума цифр числа 12345: 15
"""
print_task(6)

input_value = input("Введіть натуральне число:")
sum_value = 0
if not input_value.isdigit() or int(input_value) <= 0:
    print("Ви ввели ненатуральне число!")
else:
    for v in input_value:
        sum_value += int(v) 
    print(f"Сума цифр {input_value}: {sum_value}")

# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""
print_task(7)

print("Введiть число бiльше 0!\nВведiть 0 для виводу сумми та завершення!\n")
digits_val = 0
while True:
    input_dig = input("Число: ")
    if not input_dig:
        print("Ви нічого не ввели! Будь ласка, введіть число.")
        continue  
    elif not input_dig.lstrip('-').isdigit():
        print(f"Ви ввели невірне {input_dig} число! Введіть чиcло бiльше 0!\nАбо введiть 0 для завершення!")
        continue  
    input_dig = int(input_dig)

    if input_dig == 0:
        break
    digits_val += input_dig 
    print(f"Поточна сума: {digits_val}")
print(f"Додавання закінчено! Загальна сума чисел: {digits_val}")     



# task 8
"""  З використанням циклу for реалізуйте гру "Вгадай число".
Початок програми написаний, гравець має 5 спроб відгадати випадкове число від 1 до 20,
яке було згенеровано за допомогою функції randint() модуля random.
У кожній спробі гравець вводить своє припущення, після чого програма повідомляє, чи
було припущення занадто великим або занадто малим, чи гравець вгадав число.
"""
print_task(8)

import random
secret_number = random.randint(1, 20)
guesses = 0
max_guesses = 5
print("Вгадайте число від 1 до 20 за 5 спроб!")
while guesses < max_guesses:
    user_v = input("Введіть число: ")
    guesses += 1
    if not user_v:
        print(f"Ви нічого не ввели! Будь ласка, введіть число від 1 до 20. Залишилось {max_guesses - guesses} спроб!")
        continue  
    elif not user_v.isdigit():
        print(f"Ви ввели невірне {user_v} число! Введіть чиcло від 1 до 20! Залишилось {max_guesses - guesses} спроб!")
        continue  
    user_v = int(user_v)
    if user_v < 1 or user_v > 20:
        print(f"Невірне число! Число повинно бути від 1 до 20! Залишилось {max_guesses - guesses} спроб!")
        continue
    elif user_v < secret_number:
        print(f"Не вгадав! Занадто мале! Залишилось {max_guesses - guesses} спроб!")
        continue
    elif user_v > secret_number:
        print(f"Не вгадав! Занадто велике! Залишилось {max_guesses - guesses} спроб!")
        continue
    else:
        print(f"Вірно це число {secret_number}! Молодець!")
        break
else:
    print(f"Ви використали всі спроби. Загадане число було {secret_number}.")

# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
print(9)
fruits = ["apple", "banana", "orange", "grape", "mango"]
new_fru = [fru for fru in fruits if fru != "orange"]
# for fru in fruits:
#     if fru == "orange":
#         continue
#     new_fru.append(fru)
print(new_fru)
    
# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
print_task(10)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [numb * numb for numb in numbers if numb % 2 == 0]
# for numb in numbers:
#     if numb % 2 == 0:
#         result.append(numb * numb)
print(result)  #  [4, 16, 36, 64, 100]
