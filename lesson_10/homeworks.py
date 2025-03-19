def average(numbers):
    """Функція знаходить середнє арифметичне у списку чисел."""
    if len(numbers) == 0:
        raise ValueError("Список порожній")
    suma = 0
    for n in numbers:
        if type(n) != int and type(n) != float:
            raise ValueError("Не всі елементи є числами")
        suma += n
    return suma / len(numbers)


def longest_word(words):
    """Функція повертає найдовше слово у списку слів."""
    if len(words) == 0:
        raise ValueError("Список порожній")
    max_word = ""
    for word in words:
        if type(word) != str:
            raise ValueError("Не всі елементи є рядками")
        if len(word) > len(max_word):
            max_word = word
    return max_word


def find_substring(str1, str2):
    """Функція шукає підрядок у рядку і повертає індекс першого входження."""
    if type(str1) != str or type(str2) != str:
        raise ValueError("Обидва параметри мають бути рядками")
    if type(str1) != str or type(str2) != str:
        raise TypeError ("Один із параметрів не рядок")
    index = -1
    for i in range(len(str1) - len(str2) + 1):
        if str1[i:i + len(str2)] == str2:
            index = i
            break
    return index
