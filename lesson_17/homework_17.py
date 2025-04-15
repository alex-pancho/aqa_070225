import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Генератори:
# Task 1.1 Напишіть генератор, який повертає послідовність парних чисел від 0 до N.

def even_numbers(n):
    """
    Generate even numbers from 0 to n inclusive.
    Args:
        n (int): The upper limit of the range.
    Yields:
        int: The next even number in the sequence.
    """
    for number in range(0, n + 1):
        if number % 2 == 0:
            yield number


# Task 1.2 Напишіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci(n):
    """
    Generate Fibonacci numbers up to n inclusive.
    Args:
        n (int): The upper limit for the Fibonacci sequence.
    Yields:
        int: The next number in the Fibonacci sequence.
    """
    current = 0
    next_value = 1
    while current <= n:
        yield current
        temp = current + next_value
        current = next_value
        next_value = temp

# Ітератори:
# Task 2.1 Реалізуйте ітератор для зворотного виведення елементів списку.

class ReverseIterator:
    """Iterator for traversing a list in reverse order."""
    
    def __init__(self, data):
        """
        Initialize the reverse iterator.
        Args:
            data (list): The list to be traversed in reverse.
        """
        self.data = data
        self.index = len(data) - 1 

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """
        Return the next element in reverse order.
        Returns:
            Any: The next element in reverse order.
        Raises:
            StopIteration: If there are no more elements to return.
        """
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value

# Task 2.2 Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

class EvenNumberIterator:
    """Iterator that returns even numbers from 0 up to a specified limit."""

    def __init__(self, n):
        """
        Initialize the iterator with an upper limit.
        Args:
            n (int): The upper limit for generating even numbers.
        """
        self.n = n
        self.current = 0

    def __iter__(self):
        """
        Return the iterator object itself.
        Returns:
             EvenNumberIterator: The iterator object.
        """
        return self

    def __next__(self):
        """
        Return the next even number in the sequence.
        Returns:
            int: The next even number in the sequence.
        Raises:
            StopIteration: If the current value exceeds the upper limit.
        """
        while self.current <= self.n:
            if self.current % 2 == 0:
                value = self.current
                self.current += 1
                return value
            self.current += 1
        raise StopIteration

# Декоратори:
# Task 3.1  Напишіть декоратор, який логує аргументи та результати викликаної функції.

def log_decorator(func):
    """
    Decorator that logs function arguments and return value.
    Args:
        func (callable): The function to be decorated.
    Returns:
        callable: The wrapped function with logging.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"Function '{func.__name__}' was called with args: {args}, kwargs: {kwargs}")
        logging.info(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

# Task 3.2  Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.

def exception_decorator(func):
    """
    Decorator that catches and handles exceptions during function execution.
    Args:
        func (callable): The function to be decorated.
    Returns:
        callable: The wrapped function with exception handling.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in '{func.__name__}': {e}")
            return f"Handled exception in '{func.__name__}': {e}"
    return wrapper

@log_decorator
def add(x, y):
    return x + y

@exception_decorator
def divide(a, b):
    return a / b

def repeat_text(text, count):
    return text * count

repeat_text = exception_decorator(repeat_text)
repeat_text = log_decorator(repeat_text)

if __name__ == "__main__":

    print("Even numbers (using next()):")
    even_gen = even_numbers(10)
    print(next(even_gen))  # 0
    print(next(even_gen))  # 2
    print(next(even_gen))  # 4
    print(next(even_gen))  # 6
    print(next(even_gen))  # 8
    print(next(even_gen))  # 10
    try:
        print(next(even_gen)) # StopIteration
    except StopIteration:
        print("StopIteration raised – no more even numbers")

    print("Even numbers (using for loop):")
    for number in even_numbers(10):
        print(number)


    print("Fibonacci numbers (using next()):")
    fib_gen = fibonacci(50)
    print(next(fib_gen))  # 0
    print(next(fib_gen))  # 1
    print(next(fib_gen))  # 1
    print(next(fib_gen))  # 2
    print(next(fib_gen))  # 3
    print(next(fib_gen))  # 5
    print(next(fib_gen))  # 8
    print(next(fib_gen))  # 13
    print(next(fib_gen))  # 21
    print(next(fib_gen))  # 34
    try:
        print(next(fib_gen))  # StopIteration
    except StopIteration:
        print("StopIteration raised – no more Fibonacci numbers")

    print("Fibonacci numbers (using for loop):")
    for number in fibonacci(50):
        print(number)


    print("Reversed list:")
    my_list = [1, 2, 3, 4, 5]
    for item in ReverseIterator(my_list):
        print(item)

    print("Even numbers from 0 to N:")
    for number in EvenNumberIterator(10):
        print(number)


    print("Testing 'add'")
    print(add(5, 3))

    print("\nTesting 'divide' (OK)")
    print(divide(10, 2))

    print("\nTesting 'divide' (error)")
    print(divide(5, 0))

    print("\nTesting 'repeat_text' (OK)")
    print(repeat_text("Hi! ", 2))

    print("\nTesting 'repeat_text' (error)")
    print(repeat_text("Oops", "nope"))
