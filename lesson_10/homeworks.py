def sum_numbers_in_list(string_list: list):
    """Повертає список сум чисел зі списку строк,
    які складаються з чисел, розділених комою."""
    if not isinstance(string_list, list):
        raise ValueError("Не можна виконати операцію.")
    if not string_list:
        raise ValueError("Список порожній! Не можна виконати операцію.")
    result = []
    for item in string_list:
        try:
            pass
            numbers = item.split(",")
            numbers = [int(num) for num in numbers]  
            result.append(sum(numbers))
        except ValueError as e:
            result.append("Не можу це зробити!")

        except AttributeError as e:
            result.append("Не можу це зробити! AttributeError")
    return result


def reverse(task_4):
    """Повертає, значення в риверсивонму порядку"""
    return task_4[::-1]

def add_numbers(a, b):
    """Додає два значення"""
    return a + b    
