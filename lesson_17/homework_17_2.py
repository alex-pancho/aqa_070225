"""Генератори:

    Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
    Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
"""
def even_numbers_generator(N):
    a = 0
    while a <= N:
        if a % 2 == 0:
            yield a
            a += 2
            
def fibonacci_generator(N):
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b
        
if __name__ == "__main__":
    for num in even_numbers_generator(10):
        print(num)
        
    
    for num in fibonacci_generator(21):
        print(num)
    
    
        
