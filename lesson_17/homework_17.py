"""
Генератори:

    Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
    Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

Ітератори:

    Реалізуйте ітератор для зворотного виведення елементів списку.
    Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

Декоратори:

    Напишіть декоратор, який логує аргументи та результати викликаної функції.
    Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
"""
import logging


# Генератор, який повертає послідовність парних чисел від 0 до N.
def even_numbers(n: int):
    for number in range(0, n + 1, 2):
        yield number


if __name__ == "__main__":
    for number in even_numbers(11):
        print(number)
    print("*" * 88)


# Генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci_gen(n: int):
    a, b = 1, 1
    while a <= n:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    n = 100
    for num in fibonacci_gen(n):
        print(num)
    print("*" * 88)


# Ітератор для зворотного виведення елементів списку.
class ReverseList():
    def __init__(self, lst: list):
        self.index = len(lst) - 1
        self.step = 1
        self.lst = lst

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            result = self.lst[self.index]
            self.index -= 1
            return result
        raise StopIteration


if __name__ == "__main__":
    list_1 = [7, 2, 3, 4, 5]
    for i in ReverseList(list_1):
        print(i)
    print("*" * 88)


# Ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenNumbers:
    def __init__(self, n: int):
        self.n = n
        self.step = 2
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > n:
            raise StopIteration
        current = self.current
        self.current += self.step
        return current


if __name__ == "__main__":
    n = 21
    for number in EvenNumbers(20):
        print(number)
    print("*" * 88)

# Логер
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Декоратор, який логує аргументи та результати викликаної функції.
def log_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__} returned: {result}")
        return result

    return wrapper


@log_decorator
def power_number(a: int, p: int):
    return pow(a, p)


if __name__ == "__main__":
    print(power_number(2, 3))
    print("*" * 88)


# Декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Exception in {func.__name__}: {type(e).__name__} - {str(e)}")
            return None

    return wrapper


@exception_handler
def divide(a: float, b: float):
    return a / b


if __name__ == "__main__":
    print(divide(10, 2))
    print(divide(10, 0))  # Логує помилку ділення на нуль і повертає None
