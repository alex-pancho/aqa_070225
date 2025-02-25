def print_task(task_number):
    print(f"\n\n---Task {task_number}---\n")


small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list

print_task(1)

unic_small_set = set(small_list)
print(unic_small_set)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list

print_task(2)

avr_smal_list = sum(small_list) / len(small_list)
print(avr_smal_list)

# task 3. Перевірте, чи є в списку big_list дублікати

print_task(3)

big_set = set(big_list)
print(
    "Так в списку є дублiкати!"
    if len(big_list) != len(big_set)
    else "Список не мiстить дублiкатiв!"
)


base_dict = {"contry": "Ukraine", "continent": "Europe", "size": 123}
add_dict = {"a": 1, "b": 2, "c": 2, "d": 3, "size": 12}

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict

print_task(4)

#  Альтернативний розв'язок
#   max_value = []
#   for value in add_dict.values():
#       max_value.append(value)
#   max_key= []
#   for key, value in add_dict.items():
#       if value == max(max_value):
#         max_key.append(key)
#    print(max_key)

max_value = max(add_dict.values())
max_key = [key for key, value in add_dict.items() if value == max_value]
print(max_key)

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику

print_task(5)

new_dict = {}
for key, value in base_dict.items():
    key, value = value, key
    new_dict[key] = value
print(new_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх

print_task(6)

sum_dict = {}
for key, value in base_dict.items():
    if key in add_dict:
        sum_dict[key] = f"{value}{add_dict[key]}"
    else:
        sum_dict[key] = value

for key, value in add_dict.items():
    if key not in sum_dict:
        sum_dict[key] = value
print(sum_dict)

# task 7.

print_task(7)

line = "Створіть множину всіх символів, які входять у заданий рядок"
line_set = set(line)
print(line_set)


# task 8. Обчисліть суму елементів двох множин, які не є спільними

print_task(8)

set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
sum_sets = sum(set_1 ^ set_2)
print(sum_sets)


# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

print_task(9)

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
sum_list = set(list_1) ^ set(list_2)
print(sum_list)

# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

print_task(10)

person_list = [
    ("Alice", 25),
    ("Boby", 19),
    ("Charlie", 32),
    ("David", 28),
    ("Emma", 22),
    ("Frank", 45),
]

person_keys = ["10-19", "20-29", "30-39", "40-49"]
person_dict = {key: [] for key in person_keys}

for name, age in person_list:
    if 10 <= age <= 19:
        person_dict["10-19"].append(name)
    elif 20 <= age <= 29:
        person_dict["20-29"].append(name)
    elif 30 <= age <= 39:
        person_dict["30-39"].append(name)
    elif 40 <= age <= 49:
        person_dict["40-49"].append(name)

print(person_dict)
