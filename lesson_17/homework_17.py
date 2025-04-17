"""
Генератори:

    Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
    Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
"""


def even_numbers(n):
    """Генератор парних чисел від 0 до N."""
    if not isinstance(n, int):
        raise TypeError("N must be an integer.")
    if n < 0:
        raise ValueError("N must be a non-negative integer.")
    for i in range(0, n + 1, 2):
        yield i


def fibonacci(n):
    """Генератор послідовності Фібоначчі до N."""
    if not isinstance(n, int):
        raise TypeError("N must be an integer.")
    if n < 0:
        raise ValueError("N must be a non-negative integer.")
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


"""
Ітератори:

    Реалізуйте ітератор для зворотного виведення елементів списку.
    Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
"""


def reverse_iterator(lst):
    """Ітератор для зворотного виведення елементів списку."""
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    if len(lst) == 0:
        raise ValueError("List is empty.")
    if len(lst) == 1:
        yield lst[0]
        return
    for i in range(len(lst) - 1, -1, -1):
        yield lst[i]


def even_iterator(n):
    """Ітератор для повернення парних чисел від 0 до N."""
    if not isinstance(n, int):
        raise TypeError("N must be an integer.")
    if n < 0:
        raise ValueError("N must be a non-negative integer.")
    for i in range(0, n + 1, 2):
        yield i


"""
Декоратори:

    Напишіть декоратор, який логує аргументи та результати викликаної функції.
    Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
"""


def log_function(func):
    """Декоратор для логування аргументів та результатів функції."""

    if not callable(func):
        raise TypeError("The provided argument must be a callable function.")

    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return wrapper


def exception_handler(func):
    """Декоратор для обробки винятків."""

    def wrapper(*args, **kwargs):
        if not callable(func):
            raise TypeError("The provided argument must be a callable function.")
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")

    return wrapper
