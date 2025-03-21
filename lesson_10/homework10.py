# 1
def multiplication_table(number):
    multiplier = 1
    result_str = ""  
    while True:
        result = number * multiplier
        if result > 25:
            break
        result_str += f"Task 1 --> {number} x {multiplier} = {result}\n"  
        multiplier += 1
    return result_str  

# 2 
def longest_in_list(words):
    return max(words, key=len)

# 3
def sum_numbers_in_list(string_list: list):
    """Повертає список сум чисел зі списку строк,
    які складаються з чисел, розділених комою."""
    # Check if our data is a list and it's not empty
    if not isinstance(string_list, list) or not string_list:
        raise ValueError


    result = []
    for item in string_list:
        # Check if items in list are strings
        if not isinstance(item, str):
            result.append("Не можу це зробити! AttributeError")
            continue 

        try:
            # Split our elements by "," and add them 
            nums = list(map(int, item.split(",")))
            result.append(sum(nums))
        # In case of invalid data like 'asas7,8,9' we can't them
        except ValueError:
            result.append("Не можу це зробити!")

    return result

# 4 
def list_of_squares(data):
    return [x**2 for x in data if x % 2 == 0]


