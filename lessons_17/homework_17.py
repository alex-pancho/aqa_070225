# Task 1:
"""
Генератор парних чисел від 0 до N
"""
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i



# Task 2:
"""
Генератор, який генерує послідовність Фібоначчі до певного числа N.
"""

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# Task 3:
"""
Ітератор для зворотного виведення елементів списку.
"""

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
    
# Task 4:
"""
Ітератор парних чисел у діапазоні від 0 до N.
"""

class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.current <= self.n:
            if self.current % 2 == 0:
                val = self.current
                self.current += 1
                return val
            self.current += 1
        raise StopIteration
    
# Task 5:
"""
Декоратор логування аргументів та результатів
"""

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик {func.__name__} з аргументами {args}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper


@logger
def add(a, b):
    return a + b

# Task 6:
"""
Декоратор для обробки винятків.
"""
def exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Сталась помилка у  {func.__name__}: {e}")
            return None
    return wrapper

@exceptions
def divide(a, b):
    return a / b


if __name__ == "__main__":

    #Task 1:
    print("Testing TASK 1")
    print("Even numbers using 'next':")
    even_gen = even_numbers(10)
    print(next(even_gen))  
    print(next(even_gen))  
    print(next(even_gen))  
    print(next(even_gen))  
    print(next(even_gen))  
    print(next(even_gen)) 

    # Task 2:
    print("Testing TASK 2")
    print("Fibonacci numbers using 'next':")
    fibonacci_num = fibonacci(40)
    print(next(fibonacci_num))  
    print(next(fibonacci_num))  
    print(next(fibonacci_num))  
    print(next(fibonacci_num))  
    print(next(fibonacci_num))  
    print(next(fibonacci_num)) 
    print(next(fibonacci_num))  
    print(next(fibonacci_num))  
    print(next(fibonacci_num))  
    print(next(fibonacci_num))  

    # Task 3:
    print("Testing TASK 3")
    print("Reversed list:")
    lst = [1, 2, 3, 4]
    for item in ReverseListIterator(lst):
        print(item)

    # Task 4:
    print("Testing TASK 4")
    print("Even numbers from 0 to N:")
    for num in EvenIterator(10):
        print(num)

    # Task 5:

    print("Testing TASK 5 'add'")
    print(add(5, 3))

    # Task 6:
    print("Testing TASK 6")
    divide(10, 0)


