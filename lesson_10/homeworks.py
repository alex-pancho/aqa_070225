
'''Рахування унікальних символів в строці
 Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, 
 інакше - False. Строку отримати за допомогою функції input()'''
 
def count_unique_characters(str_for_count:str) -> bool:
    """Functions count unique characters in string and:\n
    - returns 'True' if string contains more than 10 unique characters;\n
    - returns 'False' if string contains less than 10 unique characters.
    """
    if not isinstance (str_for_count, str):
        raise TypeError('Only \'str\' type is expected.')
    set_for_count = set(str_for_count)
    set_len = len(set_for_count)
    if set_len == 0:
        raise ValueError('Empty string is entered.')
    if set_len > 10:
        return(True)
    if set_len <= 10:
        return(False)
  
""" Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1:str, str2:str) -> int:
    """ Function checks if str1 contains str2.\n 
    Returns index (position) of the first occurrence of str2 in str1.\n
    Returns '-1' if str1 does not contain str2."""
    if not isinstance (str1, str):
        raise TypeError('Only \'str\' type is for str1.')
    if not isinstance (str2, str):
        raise TypeError('Only \'str\' type is for str2.')
    if len(str1) < len(str2):
        raise ValueError('str1 is expected to be longer than str2.')
    if str2 in str1:
        return(str1.index(str2))
    else:
        return(-1)
 
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
def pow_even_number_list(number_list:list) -> list:
    """Function returns list with power even numbers."""
    if not isinstance(number_list, list):
        raise TypeError('List type is expected.')
    pow_number_list = [number**2 for number in number_list if number % 2 == 0]
    return(pow_number_list)

if __name__ == "__main__":

# Func 1

    str_for_count = 'qwerrrrrrrrttttttyyyyyyy'
 
    print(f'Func 1: String contains more than 10 unique characters? Response: {count_unique_characters(str_for_count)}')

# Func 2

    str1 = "Hello, world!"
    str2 = "world"

    print(f'Func 2: Index of the first occurrence of str2 in str1 (-1 if str1 does not contain str2): {find_substring(str1, str2)}') # поверне 7
    
    str1 = "The quick brown fox jumps over the lazy dog"
    str2 = "cat"

    print(f'Func 2: Index of the first occurrence of str2 in str1 (-1 if str1 does not contain str2): {find_substring(str1, str2)}') # поверне -1

# Func 3

    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(f'Func 3: New list with pow even numbers: {pow_even_number_list(number_list)}')  #  [4, 16, 36, 64, 100]