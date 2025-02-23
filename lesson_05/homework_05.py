small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
unique_small_list_elements = list(set(small_list))
print("task 1. Unique elements in small_list:", unique_small_list_elements)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
avarage = sum(small_list) / len(small_list)
print("task 2. The arithemetic mean off all elelements:", avarage)

# task 3. Перевірте, чи є в списку big_list дублікати
big_list_duplicates = len(big_list) != len(set(big_list))
print("task 3. The duplicates are in the list:",big_list_duplicates)

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
largest_key = max(add_dict, key = add_dict.get)
largest_value = add_dict[largest_key]
print("task 4. The largest value of the key is:", largest_key, largest_value)

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
food_dict = {"apple":"fruit", "carrot":"vegetable", "milk":"dairy"}
swapped_dict = {}
for key, value in food_dict.items():
    swapped_dict[value] = key
print("task 5. The new food vocabulary:",swapped_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = {}
for key, value in base_dict.items():
    sum_dict[key] = value
for key, value in add_dict.items():
    if key in sum_dict:
        sum_dict[key] = str(sum_dict[key]) + " " + str(value)  
    else:
        sum_dict[key] = value  
print("task 6. Combined dicitionaries:",sum_dict)

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
unique_characters = set(line)
print("task 7. Set of all charachters in the string:",unique_characters)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
set_3 = sum(set_1 ^ set_2)
print("task 8. The sum of elements that are not common in both sets is:", set_3)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
my_list1 = [1, 2, 3, 3, 4, 5]
my_list2 = [0, 3, 4, 5, 6, 7]
set1 = set(my_list1)
set2 = set(my_list2)
result = set1 ^ set2
print("task 9. Unique elements in the set of the lists:",result)


person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

age_ranges = {}
for name, age in person_list:
    if 10 <= age <= 19:
        age_range = '10-19'
    elif 20 <= age <= 29:
        age_range = '20-29'
    elif 30 <= age <= 39:
        age_range = '30-39'
    elif 40 <= age <= 49:
        age_range = '40-49'
    else:
        continue  
    if age_range not in age_ranges:
        age_ranges[age_range] = [] 
    age_ranges[age_range].append(name)
print("task 10. The available age ranges:",age_ranges)