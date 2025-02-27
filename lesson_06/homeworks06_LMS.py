# ДЗ 6.1. Рахування унікальних символів в строці
# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()
user_str = input('Enter a symbols:')

if len(set(user_str)) > 10:
    print("ДЗ 6.1. The number of unique characters is greater than 10: True")
else:
    print("ДЗ 6.1. The number of unique characters is greater than 10: False")

# ДЗ 6.2. Цикл “Дочекайся літери”
# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
while True:
    user_words = input('Please, enter the word with lower "h" or upper "H" case:\n')
    if 'h' in user_words or 'H' in user_words:
        print('ДЗ 6.2. Great! You entered a word containing "h" or "H".')
        break
print(f'ДЗ 6.2. Your entered word: {user_words}')

# ДЗ 6.3. Забери зі списку що потрібно
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for i in lst1:
    if isinstance(i, str):
        lst2.append(i)
print('ДЗ 6.3.',lst2)

# ДЗ 6.4. Сумуємо числа
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
numbers = [1, 4, 6, 9, 11, 13]
sum_even = 0
for num in numbers:
    if num % 2 == 0:
        sum_even += num
print(f"ДЗ 6.4. The sum of the even numbers is: {sum_even}")