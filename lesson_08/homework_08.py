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
    """Повертає список сум чисел зі списку рядків, 
    які складаються з чисел, розділених комами."""
    
    # Перевіряємо, чи переданий аргумент є списком і не є порожнім
    if not isinstance(string_list, list) or not string_list:
        raise ValueError("Очікується непорожній список рядків")
    
    result = []
    
    for item in string_list:
        # Перевіряємо, чи item є рядком
        if not isinstance(item, str):
            result.append("Не можу це зробити!")
            continue

        try:
            # Розділяємо рядок за комами, перетворюємо на числа і сумуємо
            numbers = list(map(int, item.split(",")))
            result.append(sum(numbers))
        except ValueError:
            result.append("Не можу це зробити!")
    
    return result


# Тестові виклики функції
if __name__ == "__main__":
    print(sum_numbers_in_list(["1,2,3", "4,0,6"]))  # [6, 10]
    print(sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"]))  # [6, "Не можу це зробити!", 10]
    print(sum_numbers_in_list(["1,2,3,4", 7]))  # [10, "Не можу це зробити!"]
    try:
        print(sum_numbers_in_list([]))  # ValueError
    except ValueError as e:
        print(e)
    try:
        print(sum_numbers_in_list("21"))  # ValueError
    except ValueError as e:
        print(e)
