"""
Генератори:

    Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
    Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
"""


def par_num(n: int) -> int:
    for i in range(0, n + 1, 2):
        yield i 


def fibanachi(n: int) -> int:
    x, y = 0, 1
    while x <= n:
        yield x
        x, y = y, x + y


"""
Ітератори:

    Реалізуйте ітератор для зворотного виведення елементів списку.
    Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
"""


class revers_iter:
    def __init__(self, data: list):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value


class par_num_iter:
    def __init__(self, n: int):
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


"""
Декоратори:

    Напишіть декоратор, який логує аргументи та результати викликаної функції.
    Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
"""


def log_args_result(func):
    def wrapper(*args, **kwargs):
        print("Виклик функції:", func.__name__)
        print("Аргументи:", args, kwargs)
        result = func(*args, **kwargs)
        print("Результат:", result)
        return result
    return wrapper


def hande_except(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("Сталася помилка у функції:", func.__name__)
            print(" Повідомлення:", e)
            return None
    return wrapper







if __name__ == "__main__":

    print("Перевірка генератора парних чисел:")
    for num in par_num(10):
        print(num, end=" ")
    print("\n")

    print("Перевірка генератора Фібоначчі:")
    for num in fibanachi(15):
        print(num, end=" ")
    print("\n")

    print("Перевірка ітератора зворотнього виведення:")
    data = [1, 2, 3, 4]
    rev = revers_iter(data)
    for item in rev:
        print(item, end=" ")
    print("\n")

    print("Перевірка ітератора парних чисел:")
    for num in par_num_iter(8):
        print(num, end=" ")
    print("\n")

    @hande_except
    @log_args_result
    def sum_num(a, b):
        return a + b
    print("Перевірка логування та результатів (успішний випадок):")
    sum_num(3, 4)
    print("\nПеревірка логування та обробки винятку (типи не сумісні):")
    sum_num(3, "4")