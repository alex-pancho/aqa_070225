import math

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(n)

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def unique_elements(lst):
    seen = set()
    unique_list = []
    for item in lst:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci number is not defined for negative indices")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def sum_numbers_in_list(string_list: list):
    
    if not isinstance(string_list, list) or not string_list:
        raise ValueError("Очікується непорожній список рядків")
    
    result = []
    
    for item in string_list:
        if not isinstance(item, str):
            result.append("Не можу це зробити!")
            continue

        try:
            numbers = list(map(int, item.split(",")))
            result.append(sum(numbers))
        except ValueError:
            result.append("Не можу це зробити!")
    
    return result

