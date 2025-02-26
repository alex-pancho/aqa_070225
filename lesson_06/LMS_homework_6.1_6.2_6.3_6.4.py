# ДЗ 6.1. Рахування унікальних символів в строці
""" Порахувати кількість унікальних символів в строці. 
Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()
"""
print ("\n Task 6.1 ")
line = input('Ведіть стрічку символів \n')
unique_char_count = 0
for char in line:
    if line.count(char) == 1:
        unique_char_count += 1
print("True" if unique_char_count > 10 else "False")

# ДЗ 6.2. Цикл “Дочекайся літери”
""" Напишіть цикл, який буде вимагати від користувача ввести слово,
в якому є літера "h" (враховуються як великі так і маленькі). 
Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
"""
print ("\n Task 6.2")
while True: 
    word = input('Ведіть слово з літерою h/H \n')
    if 'h' in word or 'H' in word:
        print("Good job!")
        break
       
# ДЗ 6.3. Забери зі списку що потрібно
""" Є list з даними 
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. 
Напишіть код, який свормує новий list (наприклад lst2), 
який містить лише змінні типу стрінг, які присутні в lst1.
Данні в лісті можуть бути будь якими
"""
print ("\n Task 6.3")
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = [element for element in lst1 if type(element) == str]
print(lst2)

# ДЗ 6.4. Сумуємо числа
""" Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
"""
print ("\n Task 6.4")
numbers_list = [1, 3, 5, 4, 8, 1, 9, -6]
suma =  sum (num for num in numbers_list if num % 2 == 0)
print(suma)