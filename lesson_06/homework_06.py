# task 1
alien_color = 'green'
if alien_color == 'green':
    print("Гравець щойно заробив 5 балів.")

# task 2
alien_color = 'yellow'  # щоб спрацювала else
if alien_color == 'green':
    print("Гравець щойно заробив 5 балів.")
else:
    print("Гравець щойно заробив 10 балів.")

# task 3-4
alien_colors = ['green', 'yellow', 'red']
for alien_color in alien_colors:
    if alien_color == 'green':
        print("Гравець щойно заробив 5 балів.")
    elif alien_color == 'red':
        print("Гравець щойно заробив 15 балів.")
    else:
        print("Гравець щойно заробив 10 балів.")

# task 5
print("\n=== Начинки для піци ===")
while True:
    topping = input("Введіть начинку для піци (або 'quit' для завершення): ")
    if topping.lower() == 'quit':
        break
    print(f"Додаємо {topping} до вашої піци.")

# task 6
print("\n=== Сума цифр числа ===")
number = input("Введіть натуральне число: ")
sum_digits = 0
for digit in number:
    sum_digits += int(digit)
print(f"Сума цифр числа {number}: {sum_digits}")

# task 7
print("\n=== Калькулятор з підсумком ===")
total = 0
while True:
    num = int(input("Введіть число (0 для завершення): "))
    if num == 0:
        break
    total += num
print(f"Сума всіх чисел: {total}")

# task 8
print("\n=== Гра 'Вгадай число' ===")
import random
secret_number = random.randint(1, 20)
max_guesses = 5
print("Вгадайте число від 1 до 20 за 5 спроб!")

for guess in range(max_guesses):
    user_guess = int(input(f"Спроба {guess + 1}: "))
    if user_guess < secret_number:
        print("Занадто мало.")
    elif user_guess > secret_number:
        print("Занадто багато.")
    else:
        print("Вітаємо! Ви вгадали число.")
        break
else:
    print(f"Ви програли. Загадане число було: {secret_number}")

# task 9
print("\n=== Список фруктів без 'orange' ===")
fruits = ["apple", "banana", "orange", "grape", "mango"]
for fruit in fruits:
    if fruit == "orange":
        continue
    print(fruit)

# task 10
print("\n=== Квадрати парних чисел ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x**2 for x in numbers if x % 2 == 0]
print(result)  # [4, 16, 36, 64, 100]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = sum(num for num in numbers if num % 2 == 0)
print("Сума парних чисел:", even_sum)

