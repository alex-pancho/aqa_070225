# ДЗ 6.1. Рахування унікальних символів в строці
print("\n Task 1")
data  = input("Please provide your data:  ")
unique_chars = len(set(data))
print(unique_chars >= 10)

# ДЗ 6.2. Цикл “Дочекайся літери”
print("\n Task 2")
while True:
    word = input("Please provide a word to check it --> ")
    if 'h' in word.lower():
        print("You have provided a word with letter 'h'")
        break
    else:
        print("Provide new word")

# ДЗ 6.3. Забери зі списку що потрібно
print("\n Task 3")
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = [x for x in lst1 if isinstance(x, str)]
print(lst2)

# ДЗ 6.4. Сумуємо числа
print("\n Task 4")
lst3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = sum(x for x in lst3 if x % 2 == 0)
print(count) 

