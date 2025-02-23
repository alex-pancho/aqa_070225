small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
print("\n Task 01")
print(f"Унікальні елементи в списку small_list {list(set(small_list))}")

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
print("\n Task 02")
print(f"Cереднє арифметичне всіх елементів у списку small_list ≈ {round((sum(small_list) / len(small_list)), 4)}")

# task 3. Перевірте, чи є в списку big_list дублікати
print("\n Task 03")
if len(big_list) > len(set(big_list)):
    print("У списку big_list є дублікати.")
else:
    print("У списку big_list немає дублікатів.")

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
print("\n Task 04")
max = 0
for element in add_dict:
    if add_dict[element] > max:
        max = add_dict[element]
        key = element
print(f"Ключ з максимальним значенням у словнику add_dict - {key}")

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
print("\n Task 05")
new_dict = {}
for element in add_dict:
    if add_dict[element] in new_dict:
        pass
    else:
        new_dict[add_dict[element]] = element
print(new_dict)
# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
print("\n Task 06")
sum_dict = base_dict
for element in add_dict:
    if element not in sum_dict:
        sum_dict[element] = add_dict[element]
    else:
        dub_key_value = str(sum_dict.pop(element))
        sum_dict[element] = str(add_dict[element]) + ", " + dub_key_value
print(f"Новий словник sum_dict - {sum_dict}")


# task 7.
print("\n Task 07")
line = "Створіть множину всіх символів, які входять у заданий рядок"
new_set =set(line)
print(f"Множина всіх символів - {new_set}")

# task 8. Обчисліть суму елементів двох множин, які не є спільними
print("\n Task 08")
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
print(f"Cума елементів двох множин, які не є спільними - {sum(set_1^set_2)}")

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
print("\n Task 09")
list1 = [1, 2, 2, 3, 4]
list2 = [3, 4, 5, 6, 6]
list1.extend(list2)
unique_set = set()
for element in list1:
    if list1.count(element) == 1:
        unique_set.add(element)
print (unique_set)


person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
print("\n Task 10")
requested_dict = {}
list_under_10 = []
list_10_19 = []
list_20_29 = []
list_30_39 = []
list_40_49 = []
list_over_50=[]
for element in person_list:
    if element[-1] < 10:
        list_under_10.append(element[0])
        requested_dict['<10'] = list_under_10
    elif  element[-1] >= 10 and element[-1]<20:
        list_10_19.append(element[0])
        requested_dict['10-19'] = list_10_19
    elif  element[-1] >= 20 and element[-1]<30:
        list_20_29.append(element[0])
        requested_dict['20-29'] = list_20_29
    elif  element[-1] >= 30 and element[-1]<40:
        list_30_39.append(element[0])
        requested_dict['30-39'] = list_30_39
    elif  element[-1] >= 40 and element[-1]<50:
        list_40_49.append(element[0])
        requested_dict['40-49'] = list_40_49
    else:
        list_over_50.append(element[0])
        requested_dict['>=50'] = list_over_50
print(requested_dict)

# Пошук автомобіля
# Exists some car data with color, year, engine_volume, car type , price
# We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
# write code that will help us to get cars that satisfy search_criteria.
# Cars should be sorted by price ascending.
# We should print up to five (5) first found elements
print("\n ДЗ 5.1. Пошук автомобіля")
car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)}
  
"""
  'test1': ('gray', 2017, 1.6, 'pickup', 36000),
  'test2': ('silver', 2017, 1.6, 'pickup', 36000),
  'test3': ('gray', 2017, 1.6, 'pickup', 36000),
  'test4': ('silver', 2017, 1.6, 'pickup', 36000),
  'test5': ('gray', 2017, 1.6, 'pickup', 36000),
  'test6': ('silver', 2017, 1.6, 'pickup', 36000)}
"""
search_criteria = (2017, 1.6, 36000)

count = 0
satisfied_search_dict = {}
for key in car_data:
    satisfy_search_criteria = True
    for element  in search_criteria:
        if element in car_data[key]:
            pass
        else:
            satisfy_search_criteria =False
    if satisfy_search_criteria == True:
        satisfied_search_dict[key] = car_data[key]
        count += 1
satisfied_search_list = list(satisfied_search_dict.items())
if count == 0: 
    print("Немає авто, які відповідають усім критеріям пошуку")
else:
    print(f"Aвто, які відповідають усім критеріям пошуку:")
    for element in satisfied_search_list[:5]:
        print(element)

count = 0
satisfied_search_dict = {}
for key in car_data:
    for element  in search_criteria:
        if element in car_data[key]:
            satisfied_search_dict[key] = car_data[key]
            count += 1
satisfy_search_dict_sorted = list(sorted(satisfied_search_dict.items(), key=lambda x:[-1]))
satisfied_search_list = list(satisfied_search_dict.items())
if count == 0: 
    print("Немає авто, які відповідають хоч одному критерію пошуку")
else:
    print(f"Aвто, які відповідають хоч одному критерію пошуку:")
    for element in satisfied_search_list[:5]:
        print(element)

#ДЗ 5.2. Лист кортежiв ( List of tuples)
    # Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result
print("\n ДЗ 5.2. Лист кортежiв")
people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
people_records.insert(0,"Add your new record at the beginning of the given list")
people_records.insert(1,  people_records.pop(5))
people_records.insert(5, people_records.pop(2))
#element1 = people_records[1]
#element5 = people_records[5]
#people_records[1] = element5
#people_records[5] = element1
for element in people_records:
    print(element)

records_to_be_verified = [6, 10, 13]
for i in records_to_be_verified:    
    if people_records[i][2] >= 30:
        print(f"index {i} {people_records[i][0]} {people_records[i][1]} >= 30")
    else:
        print(f"index {i} {people_records[i][0]} {people_records[i][1]} < 30")