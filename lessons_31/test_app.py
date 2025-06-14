import pytest
import allure
from app import *

@allure.feature("Math Operations")
@allure.story("Addition")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Test basic addition logic")
def test_add():
    with allure.step("Add 2 + 3"):
        result = add(2, 3)
        allure.attach(str(result), name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result == 5

@allure.feature("Math Operations")
@allure.story("Subtraction")
@allure.severity(allure.severity_level.NORMAL)
def test_subtract():
    with allure.step("Subtract 10 - 4"):
        result = subtract(10, 4)
        assert result == 6

@allure.feature("Math Operations")
@allure.story("Multiplication")
@allure.severity(allure.severity_level.NORMAL)
def test_multiply():
    with allure.step("Multiply 3 * 4"):
        result = multiply(3, 4)
        assert result == 12

@allure.feature("Math Operations")
@allure.story("Division")
@allure.severity(allure.severity_level.CRITICAL)
def test_divide():
    with allure.step("Divide 10 / 2"):
        result = divide(10, 2)
        assert result == 5.0

@allure.feature("Math Operations")
@allure.story("Division by Zero")
@allure.severity(allure.severity_level.BLOCKER)
def test_divide_by_zero():
    with allure.step("Expect ValueError when dividing by zero"):
        with pytest.raises(ValueError, match="Cannot divide by zero."):
            divide(5, 0)

@allure.feature("String Utilities")
@allure.story("Reverse String")
@allure.severity(allure.severity_level.MINOR)
def test_reverse_string():
    with allure.step("Reverse 'hello'"):
        assert reverse_string("hello") == "olleh"

@allure.feature("String Utilities")
@allure.story("Check Palindrome")
@allure.severity(allure.severity_level.NORMAL)
def test_is_palindrome_true():
    with allure.step("Check 'madam' is a palindrome"):
        result = is_palindrome("madam")
        allure.attach("madam", "Input Word", allure.attachment_type.TEXT)
        assert result is True

@allure.feature("String Utilities")
@allure.story("Check Palindrome")
@allure.severity(allure.severity_level.NORMAL)
def test_is_palindrome_false():
    with allure.step("Check 'hello' is not a palindrome"):
        assert not is_palindrome("hello")

@allure.feature("List Utilities")
@allure.story("Average")
@allure.severity(allure.severity_level.NORMAL)
def test_average():
    with allure.step("Average of [2, 4, 6]"):
        assert average([2, 4, 6]) == 4.0

@allure.feature("List Utilities")
@allure.story("Average - Empty List")
@allure.severity(allure.severity_level.CRITICAL)
def test_average_empty():
    with allure.step("Raise error if list is empty"):
        with pytest.raises(ValueError, match="List is empty."):
            average([])

@allure.feature("List Utilities")
@allure.story("Max Value")
def test_find_max():
    with allure.step("Max of [1, 5, 3]"):
        assert find_max([1, 5, 3]) == 5

@allure.feature("List Utilities")
@allure.story("Max Value - Empty List")
def test_find_max_empty():
    with allure.step("Raise error if list is empty"):
        with pytest.raises(ValueError, match="List is empty."):
            find_max([])

@allure.feature("List Utilities")
@allure.story("Min Value")
def test_find_min():
    with allure.step("Min of [1, 5, 3]"):
        assert find_min([1, 5, 3]) == 1

@allure.feature("List Utilities")
@allure.story("Min Value - Empty List")
def test_find_min_empty():
    with allure.step("Raise error if list is empty"):
        with pytest.raises(ValueError, match="List is empty."):
            find_min([])
