"""
Реалізувати функцію `sum_numbers_in_list(input_list)`, яка приймає список рядків, 
де кожен рядок містить числа, розділені комами. Функція повинна повертати список 
із сум чисел для кожного рядка або відповідне повідомлення про помилку у 
випадку некоректних даних.

#### **Приклади виклику функції:**
```python
sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
sum_numbers_in_list([])  # ValueError
sum_numbers_in_list("21")  # ValueError
```
"""


'''**Коректний вхід:**
   - Якщо елемент списку є рядком із числами, розділеними комами 
   (наприклад, `"1,2,3"`), функція повинна повернути їхню суму як ціле число.
   - Наприклад, `sum_numbers_in_list(["1,2,3", "4,0,6"]) → [6, 10]`.

2. **Некоректні рядки:**
   - Якщо рядок містить некоректні символи (наприклад, `"4/0,6"`, `"asas7,8,9"`), 
   функція повинна повернути `"Не можу це зробити!"` для цього елемента.

3. **Некоректні типи:**
   - Якщо елемент списку **не є рядком** (наприклад, число, функція або словник), 
   функція повинна повертати `"Не можу це зробити! AttributeError"`.

4. **Порожній список:**
   - Якщо передано порожній список `[]`, функція повинна викликати `ValueError`.

5. **Неправильний тип вхідних даних:**
   - Якщо передано не список (наприклад, `"21"` або `3`), функція повинна 
   викликати `ValueError`.'''


def sum_numbers_in_list(string_list: list):
    """Повертає список сум чисел зі списку строк,
    які складаються з чисел, розділених комою."""
    result = []
    #перевіряємо умову 5: якщо передано не список
    if not isinstance(string_list, list) :
        raise ValueError("Не список")
    #перевіряємо умову 4: якщо передано порожній список
    if len(string_list) == 0 :
        raise ValueError("Список порожній")
    # ітеруємо по елементах списку
    for item in string_list:
        #перевіряємо умову 3: якщо елемент списку не є рядком
        if not isinstance(item, str):
            result.append("Не можу це зробити! AttributeError")
            #якщо елемент не рядок, переходимо до наступного елемента string_list
            continue
        else:
            #якщо елемент рядок, робимо спробу виконати умову 1
            try:
                suma = 0
                splitted_string = item.split(",")
                for i in splitted_string:
                    suma += int(i)
                result.append(suma)
            #Якщо рядок містить некоректні символи, виконуємться умова 2
            except ValueError as e:
                result.append("Не можу це зробити!")
    
    return result


if __name__ == "__main__":
    output = sum_numbers_in_list(["1,2,3", "4,0,6"])
    print(output)

    output = sum_numbers_in_list(["1,2,3", "4/0,6", "asas7,8,9"])
    print(output)

    output = sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])
    print(output)

    output = sum_numbers_in_list(["1,2,3,4", 7])
    print(output)

    #output = sum_numbers_in_list([])
    #print(output)

    output = sum_numbers_in_list("21")
    print(output)
    """
    sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
    sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
    sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
    sum_numbers_in_list([])  # ValueError
    sum_numbers_in_list("21")  # ValueError
    """