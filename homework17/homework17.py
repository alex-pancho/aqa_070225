import logging

# ================================
# Task 1 - Генераторы
# ================================

def generator_even_nums(n):
    """Генератор парних чисел від 0 до N"""
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

def generator_fibonacci(n):
    """Генератор послідовності Фібоначчі з n елементів"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# ================================
# Task 2 - Ітератори
# ================================

class ReverseIterator:
    """Ітератор, який повертає елементи списку у зворотному порядку"""
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = len(numbers) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.numbers[self.index]
        self.index -= 1
        return value

class EvenNumIterator:
    """Ітератор для парних чисел від 0 до N"""
    def __init__(self, n):
        self.current = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        val = self.current
        self.current += 2
        return val


# ================================
# Task 3 - Декоратори
# ================================

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_args(func):
    """Декоратор логування аргументів і результату функції"""
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

def handle_exceptions(func):
    """Декоратор, який перехоплює винятки та обробляє їх"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Exception in {func.__name__}: {e}")
            return None
    return wrapper

@log_args
def add(a, b):
    return a + b

@handle_exceptions
def divide(a, b):
    return a / b


if __name__ == '__main__':
    print("=== Task 1.1 - Парні числа до N ===")
    for number in generator_even_nums(10):
        print(number)

    print("\n=== Task 1.2 - Фібоначчі ===")
    for number in generator_fibonacci(10):
        print(number)

    print("\n=== Task 2.1 - Реверс списку ===")
    numbers = [1, 2, 3, 4, 5]
    reverse_iter = ReverseIterator(numbers)
    for num in reverse_iter:
        print(num)

    print("\n=== Task 2.2 - Парні числа ітератором ===")
    even_nums = EvenNumIterator(10)
    for num in even_nums:
        print(num)

    print("\n=== Task 3.1 - Декоратор логування ===")
    add(2, 3)
    add(5, 9)

    print("\n=== Task 3.2 - Декоратор обробки винятків ===")
    print("Result 1:", divide(10, 2))
    print("Result 2:", divide(5, 0))
    print("Result 3:", divide("a", 3))