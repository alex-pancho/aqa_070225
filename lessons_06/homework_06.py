# Task 6.1
""" Порахувати кількість унікальних символів в строці. 
Якщо їх більше 10 - вивести в консоль True, інакше - False. 
Строку отримати за допомогою функції input()
"""
print("Task 6.1")

line = input("Введіть символи: \n")
char_count = 0
for char in line:
        if line.count(char) == 1:
          char_count += 1
print("True" if char_count > 10 else "False")
print("\n")


#Task 6.2 
"""Напишіть цикл, який буде вимагати від користувача ввести слово,
 в якому є літера "h" (враховуються як великі так і маленькі). 
Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
"""
print("Task 6.2")

while True:
     word = input("Введіть слово в якому є літера h/H \n")
     if 'h' in word or 'H' in word:
          print("Yesssir")
          break

print("\n")     


#Task 6.3
"""Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. 
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1. 
Данні в лісті можуть бути будь якими
"""

print("Task 6.3")

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = [element for element in lst1 if type(element) == str]
print(lst2)
print("\n")

#Task 6.4
"""ЄЄ ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
"""

print("Task 6.4")

list = [1, 3, 4, 6, 7, 8, 9, 4, 10]
sum = sum(num for num in list if num % 2 == 0)
print(f'Сума парних чисел: {sum}')