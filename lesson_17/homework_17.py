import logging


""" 1. Генератори"""
"""Task 1.1 Напишіть генератор, який повертає послідовність парних чисел від 0 до N"""

def even_numbers_generator(N):
    """Generates even numbers from 0 to N (inclusive)."""
    for number in range(0, N + 1, 2):
        yield number

"""Task 1.2 Створіть генератор, який генерує послідовність Фібоначчі до певного числа N."""

def fibonacci_generator(N):
    """Generates Fibonacci numbers up to a given mubber N (inclusive)."""
    a, b = 0, 1 #first 2 numbers 
    while a <= N:
        yield a
        a, b = b, a + b # b -> a, a + b -> b

"""2. Ітератори"""
"""Task 2.1 Реалізуйте ітератор для зворотного виведення елементів списку."""
class ReversedList:
    def __init__(self, list):
        self.list = list
        self.index = len(list)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.list[self.index]
            
"""Task 2.2 Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N."""
class EvenNumbers:
    def __init__(self, last_number):
        self.current_number = 0
        self.last_number = last_number

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_number > self.last_number:
            raise StopIteration
        even_number = self.current_number
        self.current_number += 2
        return even_number

"""3. Декоратори"""
"""Task 3.1 Напишіть декоратор, який логує аргументи та результати викликаної функції."""

def log_decorator(func):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(msg=f'Function arguments: args = {args}, kwargs = {kwargs}')
        logger.info(msg=f'Function result: {result}')
        return result
    return wrapper

@log_decorator
def add(x, y):
    return x + y

"""Task 3.2 Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції."""

def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            return f"Error for {func.__name__}: {e}"
    return wrapper

@exception_decorator
def divide_numbers(a, b):
    return a / b

if __name__ == '__main__':
    print('Task 1.1. Generates even numbers from 0 to N (inclusive):')
    for number in even_numbers_generator(20):
        print(number)
    print('Task 1.2. Generates Fibonacci numbers up to a given mubber N (inclusive):')
    for number in fibonacci_generator(55):
        print(number)
    print('Task 2.1. Iterator: reversed list')
    my_list = ReversedList([1,2,3,4,5,6,7])
    for i in my_list:
        print(i)
    print('Task 2.2. Iterator: even numbers')
    my_range = EvenNumbers(10)
    for i in my_range:
        print(i)
    print('Task 3.1. Logger decorator')
    add(5, 6)
    add(y = 10, x = 5)
    print('Task 3.2. Exception decorator')
    print(divide_numbers(5, 2))
    print(divide_numbers(5, 0))
    print(divide_numbers('a', 4))