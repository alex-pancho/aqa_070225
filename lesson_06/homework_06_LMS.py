'''ДЗ 6.1. Рахування унікальних символів в строці
Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, 
інакше - False. Строку отримати за допомогою функції input()'''

str_for_count = input('Enter any string to check if it contains more or less than 10 unique characters: ')
set_for_count = set(str_for_count)

set_len = len(set_for_count)

if set_len > 10:
    print(True, f'(TASK 6.1: String incudes {set_len} unique characters)')
if set_len <= 10:
    print(False, f'(TASK 6.1: String incudes {set_len} unique characters)')

print('-----------------------------------------------------------------------')

'''ДЗ 6.2. Цикл “Дочекайся літери”
Напишіть цикл, який буде вимагати від користувача ввести слово, 
в якому є літера "h" (враховуються як великі так і маленькі). 
Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".'''

str_from_user = input('TASK 6.2: Enter any string that contains letter \'h\' or \'H\': ')

while 'h' not in str_from_user and 'H' not in str_from_user: 
    print('TASK 6.2: Your string does not contain \'h\' or \'H\'!')
    str_from_user = input('TASK 6.2: Enter again any string that contains letter \'h\' or \'H\': ')
    
print('-----------------------------------------------------------------------')

'''ДЗ 6.3. Забери зі списку що потрібно
Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, 
які присутні в lst1. Данні в лісті можуть бути будь якими'''

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []

for item in lst1:
    if type(item) == str:
        lst2.append(item)
print(f'TASK 6.3: Here is the list only with \'str\' items: {lst2}')

print('-----------------------------------------------------------------------')

'''ДЗ 6.4. Сумуємо числа
Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті'''

numbers_list = [2, 9, 10, 56, 3, 6, 8, 22, 101, 100, 66, 57, 56, 57]

for number in numbers_list:
    if number % 2 != 0:
        numbers_list.remove(number)
    even_numbers_sum = sum(numbers_list)
print(f'TASK 6.4: The sum of even numbers is: {even_numbers_sum}')

print('-----------------------------------------------------------------------')