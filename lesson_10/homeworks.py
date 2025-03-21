def sum_numbers_in_list(string_list: list):
    """Повертає список сум чисел зі списку строк,
    які складаються з чисел, розділених комою."""
    result = []

    if not string_list or not isinstance(string_list, list):
        raise ValueError("Не можу це зробити! Очікую список чисел")
    for item in string_list:
        try:
            result.append(sum(int(x) for x in item.split(",")))
        except AttributeError as e:
            result.append("Не можу це зробити! AttributeError")
        except ValueError as e:
            result.append("Не можу це зробити!")

    return result


def multiplication_table(number, max_value):
    # Initialize the appropriate variable
    multiplier = 1
    table = []
    # Complete the while loop condition.
    if not isinstance(number,int) or not isinstance(max_value,int):
        raise TypeError("Не можу це зробити! Введіть число та максимальне значення")
    while multiplier <= 10:
        result = number * multiplier
        # десь тут помилка, а може не одна
        if result > max_value:
            break
        table.append(f"{multiplier} * {number} = {result}")
        multiplier += 1
    return table


def list_sum(list_of_numbers: list[int]):
    result = 0
    if not isinstance(list_of_numbers,list) :
        raise ValueError("Не можу це зробити! Очікую список чисел")
    if len(list_of_numbers)==0:
        raise TypeError("Не можу це зробити! Очікую список чисел")
    for i in list_of_numbers:
        if not isinstance(i, int):
            raise TypeError(f"Очікую лише цілі числа, але отримав: {type(i).__name__}")
        result += i
    return result


if __name__ == "__main__":
    print(multiplication_table(1, 4))
    multiplication_table(0,0)
    print(list_sum(["1", "2"]))
