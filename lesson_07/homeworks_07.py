# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та виправити\доповнити.
"""
from re import search


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    max_value = 25
    # Complete the while loop condition.
    while multiplier <= 10:
        result = number * multiplier
        # десь тут помилка, а може не одна
        if result > max_value:
            break

        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def sum_two_numbers(num_1: int, num_2: int):
    return num_1 + num_2


first_num = 5
second_num = 6
print(f"\n{first_num} + {second_num} = {sum_two_numbers(first_num, second_num)}\n")

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def list_sum(list_of_numbers: list[int]):
    result = 0
    for i in list_of_numbers:
        result += i
    return result


list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Сума чисел {list_num} дорівнює: {list_sum(list_num)}\n")
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def revers_string(string: str):
    return string[::-1]


word = "Hello"
print(f"{word} у зворотному порядку: {revers_string(word)}\n")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def longest_word(list_of_words: list[str]):
    return max(list_of_words, key=len)


list_words = ["apple", "banana", "orange", "grapes", "melon", "pineapple", "berry", "cherry"]
print(f"Найдовше слово в списку: {longest_word(list_words)}\n")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str_1: str, str_2: str) -> int:
    return str_1.find(str_2)


str_1 = "Hello, world!"
str_2 = "world"
print(find_substring(str_1, str_2))  # поверне 7

str_1 = "The quick brown fox jumps over the lazy dog"
str_2 = "cat"
print(find_substring(str_1, str_2), "\n")  # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""


# task 7
def get_squared_evens(list_of_numbers: list[int]) -> list[int]:
    """Returns a list of squares of even numbers from the list.

    :param list_of_numbers: A list of integers.
    :return: A new list containing the squares of even numbers only.
    """
    return [number ** 2 for number in list_of_numbers if number % 2 == 0]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# print(get_squared_evens(numbers))  # [4, 16, 36, 64, 100]


# task 8
def filter_and_sort_cars(
        dict_of_cars: dict[str: tuple],
        search_criteria: list[int | float]
) -> list[tuple[str, tuple]]:
    """
    Filters a dict of cars based on year, engine_volume and price.
    Sort a dict by price.

    Cars are selected based on the following conditions:
    - The value in the second field of the tuple (value(1)) must be at least search_criteria[0].
    - The value in the third field of the tuple (value[2]) must be at least search_criteria[1].
    - The value in the fifth field of the tuple (value[4]) must be at most search_criteria[2].

    :param dict_of_cars: A dict of cars{key - car brand: tuple(str(color of the car), int(year), float(engine volume),
    str(car type), int(price)}
    :param search_criteria: int(year), float(engine volume), int(price)
    :return:A sorted list of tuples (car name, list of characteristics).
    """
    return sorted(
        ((key, value) for key, value in dict_of_cars.items()
         if value[1] >= search_criteria[0]
         and value[2] >= search_criteria[1]
         and value[4] <= search_criteria[2]),
        key=lambda car: car[1][4]
    )


car_data = {
    'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
    'Audi': ('black', 2020, 2.0, 'sedan', 55000),
    'BMW': ('white', 2018, 3.0, 'suv', 70000),
    'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
    'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
    'Honda': ('red', 2017, 1.5, 'sedan', 30000),
    'Ford': ('green', 2019, 2.3, 'suv', 40000),
    'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
    'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
    'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
    'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
    'Kia': ('white', 2020, 2.0, 'sedan', 28000),
    'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
    'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
    'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
    'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
    'Jeep': ('green', 2021, 3.0, 'suv', 50000),
    'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
    'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
    'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
    'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
    'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
    'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
    'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
    'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
    'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
    'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
    'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
    'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
    'Acura': ('white', 2017, 2.4, 'suv', 40000),
    'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
    'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
    'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
    'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
    'Ram': ('black', 2019, 5.7, 'pickup', 40000),
    'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
    'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
    'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
    'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}
search_criteria = [2017, 1.6, 36000]


# print(filter_and_sort_cars(car_data, search_criteria))


# task 9
def title_words_count(text: str) -> int:
    """Counts the number of words in a text that start with an uppercase letter.

    :param text: Text string.
    :return: Number of words starting with an uppercase letter.
    """
    return sum(1 for word in text.split() if word[0].isupper())


text = "By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher"


# print(f"{title_words_count(text)} слів починаються з великої літери в тексті\n")


# task 10
def remainder_of_division(num_1: int, num_2: int) -> int:
    """Calculates the remainder of dividing the first number by the second.

    :param num_1: Dividend (an integer).
    :param num_2: Divisor (an integer).
    :return: The remainder of num_1 divided by num_2.
    """
    return num_1 % num_2


num_1 = 5
num_2 = 2
# print(f"Остача від ділення {num_1} на {num_2} = {remainder_of_division(num_1,num_2)}")
