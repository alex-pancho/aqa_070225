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
    """Повертає список сум чисел зі списку строк,
    які складаються з чисел, розділених комою."""
    num_list = []
    if not isinstance(string_list,list):
        raise ValueError("List is expected as input")
    if len(string_list) == 0:
        raise ValueError("List is empty")
    for i in string_list:
        try:
            numbers = map(int, i.split(','))
            num_list.append(sum(numbers))
        except ValueError:
            num_list.append("Не можу це зробити!")
        except AttributeError:
            num_list.append("Не можу це зробити! AttributeError")
    return num_list


if __name__ == "__main__":
    output = sum_numbers_in_list(["1,2,3", "4,0,6"])
    print(output)

    output = sum_numbers_in_list(["1,2,3", "4/0,6", "asas7,8,9"])
    print(output)

# print(sum_numbers_in_list(["1,2,3", "4,0,6"]))  # [6, 10]
# print(sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"]))  # [6, "Не можу це зробити!", 10]
# print(sum_numbers_in_list(["1,2,3,4", 7]))  # [10, "Не можу це зробити! AttributeError"]
# print(sum_numbers_in_list([]))  # ValueError
# print(sum_numbers_in_list("21"))  # ValueError
