import pytest
from homework_07 import (
    add_numbers,
    average,
    reverse_string,
    longest_word,
    find_substring,
)

def test_add_numbers_positive():
    assert add_numbers(2, 3) == 5

def test_add_numbers_negative():
    assert add_numbers(-4, -6) == -10

def test_average_regular_list():
    assert average([1, 2, 3, 4, 5]) == 3.0

def test_average_empty_list():
    assert average([]) == 0

def test_average_single_element():
    assert average([10]) == 10.0

def test_reverse_string_regular():
    assert reverse_string("hello") == "olleh"

def test_reverse_string_empty():
    assert reverse_string("") == ""

def test_longest_word_regular():
    assert longest_word(["apple", "banana", "cherry"]) == "banana"

def test_longest_word_tie():
    assert longest_word(["cat", "dog", "pig"]) in ["cat", "dog", "pig"]  # всі однакові

def test_longest_word_empty_list():
    assert longest_word([]) == ""

def test_find_substring_found():
    assert find_substring("hello world", "world") == 6

def test_find_substring_not_found():
    assert find_substring("quick brown fox", "cat") == -1
