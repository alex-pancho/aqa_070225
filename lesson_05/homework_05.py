small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
print("____________task 1_____________")
uniq_elements = set(small_list)
print(f"Унікальні елементи в small_list: {uniq_elements}")


# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
print("____________task 2_____________")
math_avarage = sum(small_list) / len(small_list)
print(f"Середнє арифметичне всіх елементів у списку small_list: {math_avarage}")


# task 3. Перевірте, чи є в списку big_list дублікати
print("____________task 3_____________")
if len(big_list) != len(set(big_list)):
   print("Є дублікати")
else:
   print("дубліктаів не знайдено")


base_dict = {'contry': 'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a": 1, "b": 2, "c": 2, "d": 3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
print("____________task 4_____________")


max_key = max(add_dict, key=add_dict.get)
max_value = add_dict[max_key]
print(f"Ключ '{max_key}' з максимальним значенням '{max_value}'")


# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
print("____________task 5_____________")


# порожній словник для запису нового словника, із заміненими місцями key, value
new_dict = {}


for key, value in add_dict.items():
   if value in new_dict:
       new_dict[value].append(key)
   else:
       new_dict[value] = [key]


print(f"Новий словник: {new_dict}")


# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
print("____________task 6_____________")
sum_dict = {}


# всі ключі з base_dict
for key, value in base_dict.items():
   sum_dict[key] = str(value)


print(sum_dict)  # доданий в порожній словник словник base_dict


# Додаємо ключі з add_dict
for key, value in add_dict.items():
   if key in sum_dict:
       sum_dict[key] += f", {value}"  # кома
   else:
       sum_dict[key] = str(value)


print(sum_dict)


# task 7.
print("____________task 7_____________")
line = "Створіть множину всіх символів, які входять у заданий рядок"


set_line = set(line)
print(f"Множина всіх символв: {set_line}")


# task 8. Обчисліть суму елементів двох множин, які не є спільними
print("____________task 7_____________")
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}


unique_elements = set_1 ^ set_2
print(f"Унікальні елементи в двох сетах: {unique_elements}")


sum_unique = sum(unique_elements)
print(f"Сума унікальних елементів: {sum_unique}")


# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить , то повернутий сет містить [1, 2, 5, 6]
# Знаходимо унікальні елементи, які є тільки в одному зі списків
print("____________task 9_____________")
lst_1 = [1, 2, 3, 4, 77, 88, 99]
lst_2 = [3, 4, 5, 6, 77, 78, 0]
# унікальні елементи у першому списку, і відсутні в другому
unique_in_lst_1 = set(lst_1) - set(lst_2)
print(f"Елементи, які є тільки в першому списку: {unique_in_lst_1}")
# унікальні елементи у другому списку, і відсутні в першому
unique_in_lst_2 = set(lst_2) - set(lst_1)
print(f"Елементи, які є тільки в другому списку: {unique_in_lst_2}")


person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
              ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
print("____________task 10_____________")


# dict з групами як ключем і порожніми values
age_groups = {
   "10-19": [],
   "20-29": [],
   "30-39": [],
   "40-49": []
}


# вікові групах
for name, age in person_list:
   if 10 <= age <= 19:
       age_groups["10-19"].append(name)
   elif 20 <= age <= 29:
       age_groups["20-29"].append(name)
   elif 30 <= age <= 39:
       age_groups["30-39"].append(name)
   elif 40 <= age <= 49:
       age_groups["40-49"].append(name)


print(f"Словник відсортований по віковим група: {age_groups}")

