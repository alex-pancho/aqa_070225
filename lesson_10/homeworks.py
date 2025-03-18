def sum_two_numbers(a, b):
    """
    Обчислює суму двох чисел. 

    :param a: Перше число.
    :param b: Друге число.
    :return: Сума двох чисел або повідомлення про помилку.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Для вводу доступні тільки числа!"
    return a + b


def sum_of_digits(number: int) -> int:
    """
    Функція обчислює суму всіх цифр натурального числа.

    :param number: Натуральне число, для якого потрібно обчислити суму цифр
    :return: Сума цифр числа
    """
    if not isinstance(number, int) or number < 0:
        raise ValueError("Вхід має бути натуральним числом")
    
    sum_digits = 0
    for digit in str(number):
        sum_digits += int(digit)
    return sum_digits


def swap_dict_keys_and_values(input_dict):
    """
    Функція міняє місцями ключі та значення словника.

    :param input_dict: Словник
    :return: Новий словник з поміняними місцями ключами та значеннями
    """
    
    for key in input_dict.keys():
        if not isinstance(key, (str, int, float, tuple)):
            raise TypeError(f"Ключ '{key}' даний тип не може бути використаний у якості ключа словника!")
    
    return {value: key for key, value in input_dict.items()}


def clean_string(input_string):
    """
    Функція видаляє зайві пробіли та залишає тільки один пробіл між словами.

    :param input_string: Вхідний рядок
    :return: Рядок без зайвих пробілів
    """
    if not isinstance(input_string, str):
        return str(input_string)
    return " ".join(input_string.split())