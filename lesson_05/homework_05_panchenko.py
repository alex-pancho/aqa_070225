small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list

unique_elements_small_list = list(set(small_list))
print(unique_elements_small_list)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list

mean_small_list = sum(small_list) / len(small_list)
print(mean_small_list)

# task 3. Перевірте, чи є в списку big_list дублікати

big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
has_duplicates_big_list = len(big_list) != len(set(big_list))
print(has_duplicates_big_list)

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict

add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
max_key_add_dict = max(add_dict, key=add_dict.get)
print(max_key_add_dict)

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику

reversed_add_dict = {v: k for k, v in add_dict.items()}
print(reversed_add_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
sum_dict = base_dict.copy()

for key, value in add_dict.items():
    if key in sum_dict:
        sum_dict[key] = str(sum_dict[key]) + str(value)  # Об'єднуємо як строки
    else:
        sum_dict[key] = value

print(sum_dict)

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
unique_chars = set(line)
print(unique_chars)

# task 8. Обчисліть суму елементів двох множин, які не є спільними

set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
unique_elements_sum = sum((set_1 - set_2) | (set_2 - set_1))  # Обчислюємо суму елементів, які не є спільними
print(unique_elements_sum)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]

unique_elements_once = set(list_1) ^ set(list_2)  
print(unique_elements_once)


# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]

age_ranges = {'10-19': [], '20-29': [], '30-39': [], '40-49': []}

for name, age in person_list:
    if 10 <= age <= 19:
        age_ranges['10-19'].append(name)
    elif 20 <= age <= 29:
        age_ranges['20-29'].append(name)
    elif 30 <= age <= 39:
        age_ranges['30-39'].append(name)
    elif 40 <= age <= 49:
        age_ranges['40-49'].append(name)

print(age_ranges)