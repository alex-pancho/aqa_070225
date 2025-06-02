def sum_numbers_in_list(string_list: list):
    if not isinstance(string_list, list):
        raise ValueError("Вхідні дані мають бути списком.")

    if len(string_list) == 0:
        raise ValueError("Список не може бути порожнім.")

    result = []

    for item in string_list:
        if not isinstance(item, str):
            result.append("Не можу це зробити! AttributeError")
            continue

        try:
            parts = item.split(',')
            numbers = [int(x.strip()) for x in parts]
            result.append(sum(numbers))
        except ValueError:
            result.append("Не можу це зробити!")

    return result
