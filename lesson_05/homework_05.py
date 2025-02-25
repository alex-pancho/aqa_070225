small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
small_list = set(small_list)
print(f"Унікальні елементи", small_list)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
average = sum(small_list) // len(small_list)
print(f"Середнє арифметичне {average}")

# task 3. Перевірте, чи є в списку big_list дублікати
duble = set(big_list)
duble_1 = len(duble)
print(f"Дублікати:", duble_1)


base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
add_dict_max = max(add_dict)
print(f"Максимальне значення у словнику", add_dict_max)

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
reversed_dict = {1:"a", 2:"b", 2:"c", 3:"d", 12:'size'}
print(f"Новий словник:", reversed_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = {}
for i in base_dict:
    if i in add_dict:
        sum_dict[i] = str(base_dict[i]) + str(add_dict[i])
    else:
        sum_dict[i] = base_dict[i]
for i in add_dict:
    if i not in base_dict:
        sum_dict[i] = add_dict[i]
print(f"Новий словник:", sum_dict)

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
line_set = set(line)
print(f"Множина всіх символів", line_set)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
sum_1_2 = set_1 | set_2
sum_set = sum(sum_1_2)
print(f"Сума елементів:", sum_set)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
list_1 = [('Alice', 25), ('Boby', 19), ('Charlie', 32)]
list_2 = [('David', 28), ('Emma', 22), ('Frank', 45)]
list_1.extend(list_2)
print(f"Новий список з унікалиними елементами:", list_1)

# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
age_groups = {}
for name, age in person_list:
    age_range = f'{(age // 10) * 10}-{(age // 10) * 10 + 9}'
    if age_range not in age_groups:
        age_groups[age_range] = []
    age_groups[age_range].append(name)
print(f"Діапазон та імʼя:", age_groups)



