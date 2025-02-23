small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]

# task 1. Знайдіть всі унікальні елементи в списку small_list

small_list_set = set(small_list)
print(f'TASK 1: Unique elements in list \'small_list\' are: {small_list_set}')

print('----------------------------------------------------------------')

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list

small_list_average_value = sum(small_list[:7])/len(small_list)
print(f'TASK 2: Average value of \'small_list\' is: {small_list_average_value}')

print('----------------------------------------------------------------')

# task 3. Перевірте, чи є в списку big_list дублікати

# List comprehention: [вираз for елемент in ітерабельний_об'єкт if умова]

duplicates_list = [i for i in big_list if big_list.count(i) > 1]
duplicates_set = set(duplicates_list)

if len(duplicates_set) != 0:
    print(f'TASK 3: In list \'big_list\' are present duplicates: {duplicates_set}')
else:
    print('TASK 3: In list \'big_list\' duplicates are not present')

print('----------------------------------------------------------------')

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict

all_values_add_dict = add_dict.values()

max_value = max(all_values_add_dict)

for key, value in add_dict.items():
    if value == max_value:
        print(f'TASK 4: The name of key with max value is: "{key}"')

print('----------------------------------------------------------------')

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику

# Changed all dictionary data to lists

all_items_base_dict = list(base_dict.items())

changed_all_items_base_dict = []
for i in all_items_base_dict:
    i_as_list = list(i)
    changed_all_items_base_dict.append(i_as_list)

# Switch key and value

changed_items_in_item_list = []

for i in changed_all_items_base_dict:
    index_i = changed_all_items_base_dict.index(i)
    list_with_changed_items = [] #created new sublist where switched key and value are stored
    poped_value = changed_all_items_base_dict[index_i].pop(1) # deleted value, index 1
    poped_key = changed_all_items_base_dict[index_i].pop(0) # deleted key, index 0
    list_with_changed_items.insert(0, poped_value) # inserted value to index 0 as key
    list_with_changed_items.insert(1, poped_key) # inserted key to index 1 as value
    changed_items_in_item_list.insert(index_i, list_with_changed_items)  # appended list with switched value to new list    

# Create dictionary based on list

dict_with_changed_key_and_value = dict(changed_items_in_item_list)
print(f'TASK 5: Dictionary \'base_dict\' (values: {base_dict}) with swapped \'key\' and \'value\': \n {dict_with_changed_key_and_value}')

print('----------------------------------------------------------------')

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = {}

sum_dict = base_dict

for key, value in add_dict.items():
    if key in sum_dict:
        sum_dict[key] = str(sum_dict[key]) + str(value)
    else:
        sum_dict[key] = value

print(f'TASK 6: New dictionary \'sum_dict\' value is: {sum_dict}')

print('----------------------------------------------------------------')

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"

line_set = set()

for i in line:
    line_set.add(i)
print(f'TASK 7: Set with all characters that are used in srting \'{line}\': \n{line_set}')

print('----------------------------------------------------------------')
    
# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}

logical_symmetric_difference = set_1 ^ set_2

sum_of_elements = sum(logical_symmetric_difference)

print(f'TASK 8: The sum of elements that are not common for both sets: {sum_of_elements}')

print('----------------------------------------------------------------')

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]

new_set = set(list_1) ^ set(list_2)

print(f'TASK 9: Values that are in one of the sets, but not in: {new_set}')

print('----------------------------------------------------------------')
               
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32), ('David', 28), ('Emma', 22), ('Frank', 45)]

list_of_keys = ['10-19', '20-29', '30-39', '40-49']

list_from_10_to_19 = []
list_from_20_to_29 = []
list_from_30_to_39 = []
list_from_40_to_49 = []

list_of_values = [list_from_10_to_19, list_from_20_to_29, list_from_30_to_39, list_from_40_to_49]

for i in person_list:
    i_index = person_list.index(i)
    if person_list[i_index][1] >= 10 and person_list[i_index][1] <= 19:
        list_from_10_to_19.append(person_list[i_index][0])
    if person_list[i_index][1] >= 20 and person_list[i_index][1] <= 29:
        list_from_20_to_29.append(person_list[i_index][0])        
    if person_list[i_index][1] >= 30 and person_list[i_index][1] <= 39:
        list_from_30_to_39.append(person_list[i_index][0])      
    if person_list[i_index][1] >= 40 and person_list[i_index][1] <= 49:
        list_from_40_to_49.append(person_list[i_index][0])

new_person_dict = dict(zip(list_of_keys, list_of_values))
print(f'TASK 10: Dictionary with age as \'key\' value and list of names as \'value\': \n{new_person_dict})')

print('----------------------------------------------------------------')
