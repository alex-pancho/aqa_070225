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

def even_numbers_generator(n):
    for i in range(0, n + 1, 2):
        yield i

def fibonacci_generator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
    
class ReverseListIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]
    
class EvenNumbersIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current
        self.current += 2
        return result
    
def log_arguments_and_result(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик функції: {func.__name__}")
        print(f"Аргументи: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@log_arguments_and_result
def multiply(x, y):
    return x * y



def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Виникла помилка в функції {func.__name__}: {e}")
            return None
    return wrapper

@exception_handler
def divide(x, y):
    return x / y




if __name__ == "__main__":
    for num in even_numbers_generator(10):
        print(num)
    for num in fibonacci_generator(20):
        print(num)
    reverse_iter = ReverseListIterator([1, 2, 3, 4, 5])
    print(*reverse_iter)
    even_iter = EvenNumbersIterator(10)
    print(*even_iter) 
    multiply(3, 4)
    divide(10, 0) 