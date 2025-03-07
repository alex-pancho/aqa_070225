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


def sum_numbers_in_list(string_list: list):
    if not isinstance(string_list, list):
        raise ValueError("Не можна виконати операцію.")
    if not string_list:
        raise ValueError("Список порожній! Не можна виконати операцію.")
    result = []
    for item in string_list:
        try:
            numbers = item.split(",")
            numbers = [int(num) for num in numbers]  
            result.append(sum(numbers))
            
        except ValueError as e:
            result.append("Не можу це зробити!")
        except AttributeError as e:
            result.append("Не можу це зробити! AttributeError")
    return result

if __name__ == "__main__":
    
    output = sum_numbers_in_list(["1,2,3", "4,0,6"])
    print(output)

    output = sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])
    print(output)

    output = sum_numbers_in_list(["1,2,3,4", 7])
    print(output)

    try:
        output = sum_numbers_in_list([]) 
        print(output)
    except ValueError as e:
        print("Не можу це зробити! ValueError") 

    try:
        output = sum_numbers_in_list("21") 
        print(output)
    except ValueError as e:
        print("Не можу це зробити! ValueError")
    """
    sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
    sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
    sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
    sum_numbers_in_list([])  # ValueError
    sum_numbers_in_list("21")  # ValueError
    """
