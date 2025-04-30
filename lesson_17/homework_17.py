import logging

"""Генератори
Напишіть генератор, який повертає послідовність парних чисел від 0 до N
Створіть генератор, який генерує послідовність Фібоначчі до певного числа N"""


# Генератор парних чисел від 0 до N
def even_numbers_generator(n):
    for i in range(0, n + 1, 2):
        yield i


# Генератор послідовності Фібоначчі до N
def fibonacci_generator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


"""Ітератори:


   Реалізуйте ітератор для зворотного виведення елементів списку.
   Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N."""


# Ітератор для зворотного виведення елементів списку
class ReverseListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.lst[self.index]


# Ітератор для парних чисел від 0 до N
class EvenRangeIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            val = self.current
            self.current += 1
            if val % 2 == 0:
                return val
        raise StopIteration


"""Декоратори:


   Напишіть декоратор, який логує аргументи та результати викликаної функції.
   Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
"""


# Декоратор логування аргументів і результату
def log_decorator(func):
    logger = logging.getLogger(func.__name__)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    def wrapper(*args, **kwargs):
        logger.info(f'Function arguments: args = {args}, kwargs = {kwargs}')
        result = func(*args, **kwargs)
        logger.info(f'Function result: {result}')
        return result

    return wrapper


# Декоратор обробки винятків
def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[Exception caught] {func.__name__} raised an error: {e}")
            return f"Error for {func.__name__}: {e}"

    return wrapper


@log_decorator
def add(x, y):
    return x + y


@exception_decorator
def divide_numbers(a, b):
    return a / b


if __name__ == '__main__':
    print('Task 1.1')
    for number in even_numbers_generator(15):
        print(number)

    print('\nTask 1.2.')
    for number in fibonacci_generator(55):
        print(number)

    print('\nTask 2.1')
    my_list = ReverseListIterator([1, 2, 3, 4, 5, 6, 7])
    for i in my_list:
        print(i)

    print('\nTask 2.2')
    my_range = EvenRangeIterator(10)
    for i in my_range:
        print(i)

    print('\nTask 3.1')
    add(7, 6)
    add(y=10, x=5)

    print('\nTask 3.2')
    print(divide_numbers(7, 6))
    print(divide_numbers(5, 0))
    print(divide_numbers('x', 5))
