# task 6.1
"""Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
Строку отримати за допомогою функції input()"""
string = input("Введіть строку: ")
if len(set(string)) > 10:
    print(True)
else:
    print(False)

# task 6.2
"""Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" 
(враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "h"."""
while True:
    word = input("Введіть слово, в якому є літера 'h': ")
    if "h" in word or "H" in word:
        break

# task 6.3
"""Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. 
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1. 
Данні в лісті можуть бути будь якими"""
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = [str(i) for i in lst1 if isinstance(i, str)]

# task 6.4
"""Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті"""
import random
numbers = [random.randint(1, 100) for _ in range(10)]
sum_even = sum([i for i in numbers if i % 2 == 0])
print(f"В списку {numbers} сума всіх парних чисел: {sum_even}")