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
import re

def sum_numbers_in_list(string_list: list):
    """Повертає список сум чисел зі списку строк,
    які складаються з чисел, розділених комою."""
    result = []
    if not string_list or not isinstance(string_list, list):
        raise ValueError("ValueError")
    for string in string_list:
        if not isinstance(string, str):
            result.append("Не можу це зробити! AttributeError")
            continue
        if not string:
            raise ValueError("ValueError")
        if not re.match(r"^[0-9,]+$", string):
            number_sum = "Не можу це зробити!"
            result.append(number_sum)
            continue
        number_sum = sum(map(int, string.split(",")))
        result.append(number_sum)
    return result


if __name__ == "__main__":
    output = sum_numbers_in_list(["1,2,3", "4,0,6"])
    print(output)

    output = sum_numbers_in_list(["1,2,3", "4,0,6", "asas7,8,9"])
    print(output)
"""
    output = sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
    output = sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
    output = sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
    output = sum_numbers_in_list([])  # ValueError
    output = sum_numbers_in_list("21")  # ValueError
"""
