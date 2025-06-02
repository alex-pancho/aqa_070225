import random

# task 1–4
def get_alien_points(color):
    if color == 'green':
        return 5
    elif color == 'yellow':
        return 10
    elif color == 'red':
        return 15
    else:
        return 0

# task 6
def sum_of_digits(number_str):
    return sum(int(d) for d in number_str if d.isdigit())

# task 7
def calculate_total(numbers):
    return sum(numbers)

# task 9
def fruits_without_orange(fruits):
    return [fruit for fruit in fruits if fruit != "orange"]

# task 10
def even_squares(numbers):
    return [x**2 for x in numbers if x % 2 == 0]

def even_sum(numbers):
    return sum(x for x in numbers if x % 2 == 0)

# task 8
def check_guess(secret, guesses):
    for guess in guesses:
        if guess < secret:
            feedback = "low"
        elif guess > secret:
            feedback = "high"
        else:
            return "correct"
    return f"lost:{secret}"
