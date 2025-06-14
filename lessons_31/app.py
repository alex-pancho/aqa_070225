from typing import List, Union

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a - b

def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b

def divide(a: Union[int, float], b: Union[int, float]) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def reverse_string(s: str) -> str:
    return s[::-1]

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def average(numbers: List[Union[int, float]]) -> float:
    if not numbers:
        raise ValueError("List is empty.")
    return sum(numbers) / len(numbers)

def find_max(numbers: List[Union[int, float]]) -> Union[int, float]:
    if not numbers:
        raise ValueError("List is empty.")
    return max(numbers)

def find_min(numbers: List[Union[int, float]]) -> Union[int, float]:
    if not numbers:
        raise ValueError("List is empty.")
    return min(numbers)
