"""
Декоратори:

    Напишіть декоратор, який логує аргументи та результати викликаної функції.
    Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції."""
    
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@log_decorator
def multiply(a, b):
    return a * b

def catch_exeptions(func):
    def wrapper(*args, **kwargs):
        try: 
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Помилка: {e}.")
    return wrapper
    
@catch_exeptions
def divide(a, b):
    return a / b           

if __name__ == "__main__":        
    divide(10, 0)
    multiply( 3, 4 )