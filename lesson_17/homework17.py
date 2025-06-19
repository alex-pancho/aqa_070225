# --- Генераторы ---

def even_numbers_up_to_n(n):
    """Генератор парних чисел від 0 до n включно"""
    for i in range(0, n+1, 2):
        yield i

def fibonacci_up_to_n(n):
    """Генератор чисел Фібоначчі до n"""
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# --- Ітератори ---

class ReverseListIterator:
    """Ітератор для зворотного виведення елементів списку"""
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
    """Ітератор, який повертає парні числа від 0 до n включно"""
    def __init__(self, n):
        self.n = n
        self.current = -2  # Щоб при першому next() отримати 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current > self.n:
            raise StopIteration
        return self.current

# --- Декоратори ---

def logger(func):
    """Декоратор, який логує аргументи та результат виклику функції"""
    def wrapper(*args, **kwargs):
        print(f"Виклик функції {func.__name__} з args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

def exception_handler(func):
    """Декоратор, який перехоплює та обробляє винятки"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Виняток у функції {func.__name__}: {e}")
            return None
    return wrapper

# --- Приклади використання ---

print("Генератор парних чисел до 10:")
for num in even_numbers_up_to_n(10):
    print(num, end=' ')
print("\n")

print("Генератор Фібоначчі до 50:")
for num in fibonacci_up_to_n(50):
    print(num, end=' ')
print("\n")

lst = [1, 2, 3, 4, 5]
print("Зворотній ітератор списку [1,2,3,4,5]:")
for item in ReverseListIterator(lst):
    print(item, end=' ')
print("\n")

print("Ітератор парних чисел до 10:")
for num in EvenNumbersIterator(10):
    print(num, end=' ')
print("\n")

# Приклад функції з декораторами

@logger
@exception_handler
def divide(a, b):
    return a / b

print("Виклик divide(10, 2):")
divide(10, 2)
print("Виклик divide(10, 0):")
divide(10, 0)
