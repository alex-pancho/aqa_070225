import logging

# Налаштування логера
logging.basicConfig(
    filename='logger.log',
    level=logging.INFO,
    format= '%(asctime)s -%(levelname)s - %(message)s',
    encoding='utf-8'
    )
logger = logging.getLogger()

"""
Генератори:

    Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
    Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

"""

def even_number(n):
    for number in range(n+1):
        if number % 2 == 0:
            yield number
            
def fibonacci(n):
    pre_fib_1 = 0
    pre_fib_2 = 1  
    fibonacci_number = 1
    while fibonacci_number <= n:
        yield fibonacci_number
        fibonacci_number = pre_fib_1 + pre_fib_2
        pre_fib_1 = pre_fib_2
        pre_fib_2 = fibonacci_number

"""
Ітератори:

    Реалізуйте ітератор для зворотного виведення елементів списку.
    Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
"""

class IterateElementBackward():
    def __init__(self, my_list):

        #намагаємося перевест введене значення в список
        try:
            self.my_list = list(my_list)
        #виводимо помилку якщо не вдалося зробити список
        except:
            raise TypeError("It's not a list and isn't iterable, so it can't be turned into a list.")
        #встановлюємо індекс на останній елемент
        self.current_index = len(self.my_list) -1        

    def __iter__(self): 
        return self
    
    def __next__(self):
        #якщо індекс менще 0, значить вже дійшли до початку списку, рейзимо помилку
        if self.current_index < 0:
            raise StopIteration
        #значення елемента на поточному індексі
        element = self.my_list[self.current_index] 
        # шукаємо індекс наступного елемента
        self.current_index -=1    
        # повертаємо значення елемента
        return element
        

class EvenNumbers():
    def __init__(self, n):

        #перевіряємо чи n число
        if not isinstance(n, (float, int)):
            raise ValueError("N is not a number")    
        else:
            self.n = n
                   
        #встановлюємо поточний елемент
        self.current = 0   

    def __iter__(self): 
        return self
    
    def __next__(self):
        #рейзимо помилку якщо перейшли ліміт n 
        if self.current > self.n:
            raise StopIteration
        #значення елемента на поточному індексі
        even_number = self.current
        # шукаємо наступний елемент
        self.current +=2    
        # повертаємо значення елемента
        return even_number
        
"""
Декоратори:

    Напишіть декоратор, який логує аргументи та результати викликаної функції.
    Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
"""
def decor(func):
    def wrapper(*args, **kwargs): 
        #Викликаємо основну функцію
        res = func(*args, **kwargs)
        #Повідомлення для логера
        log_message = f"Task_1 Login event aргумент: {args}, результат: {res}"
        #Логуємо 
        logger.info(log_message)
        return res
    return wrapper

@decor  
def power_to(n, b):
    return n**b

def decor_exeption(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e :
            print(f"Error occurred: {e}")
            #Повідомлення для логера
            log_message = f"Task_2 Catch exeption: сталася помилка: {e}"
            #Логуємо 
            logger.error(log_message)
    return wrapper

@decor_exeption  
def division(n):
    return 10/n


if __name__ == "__main__":
    
    even_number_1 = even_number(7)
    print(next(even_number_1))
    print(next(even_number_1))
    print(next(even_number_1))
    print(next(even_number_1))
    
    print("_________")
    fibon = fibonacci(9)
    print(next(fibon))
    print(next(fibon))
    print(next(fibon))
    print(next(fibon))
    print(next(fibon))
    print(next(fibon))
    
    print("_________")
    back_list = IterateElementBackward("qwerty")
    print(next(back_list))
    print(next(back_list))
    print(next(back_list))
    print(next(back_list))
    print(next(back_list))
    print(next(back_list))
    
    print("_________")
    even_number_2 = EvenNumbers(6)
    print(next(even_number_2))
    print(next(even_number_2))
    print(next(even_number_2))
    print(next(even_number_2))

    print("_________")
    test = power_to(3,2)
    test_2 = division("0")
    