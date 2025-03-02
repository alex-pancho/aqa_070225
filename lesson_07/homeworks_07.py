# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помилка, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
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
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 2)
print("task 2. Sum:",result)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def new_average(small_list):
  if len (small_list) == 0:
   return "Error: List is empty"
  
  average = sum(small_list) / len(small_list)
  return average

nums = [3, 1, 4, 5, 2, 5, 3]
result = new_average(nums)
print("task 3. The arithemetic mean off all elelements:", result)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(text):
    return text [::-1]

text = ("Hello")
reversed_string = reverse_string(text)
print('task 4.', reversed_string)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def long_word(words):
    return max(words, key=len)

words = ["Apple", "Banana", "Orange", "Pineapple"]
longest = long_word(words)
print("task 5. The longest word is:",longest)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
  return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"

print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
def add_pizza_toppings(toppings):
    """
    Function to process a list of pizza toppings.
    Iterates through the given list and adds each topping to the pizza.
    If 'quit' is encountered, the process stops and a final message is added.
    """
    messages = []
    for topping in toppings:
        if topping.lower() == 'quit':
            messages.append("Great choice. Thanks for building your pizza!")
            break
        messages.append(f"{topping} has been added to your pizza.")
    
    return messages

topping_list = ['ham', 'cheese', 'tomato', 'quit', 'mushrooms']
result = add_pizza_toppings(topping_list)
print('task 7.', result)

# task 8
def list_fruits(fruits):
    """
    This function accepts a list of fruits, iterates through it, and returns a new list 
    with all the fruits except 'orange'. 
    If 'orange' is encountered, it is skipped, 
    and the fruit is not added to the new list.
    """
    result = []
    for fruit in fruits:
        
        if fruit == 'orange':
            continue  
        result.append(fruit)  
    
    return result  

fruits_basket = ["apple", "banana", "orange", "grape", "mango"]
result = list_fruits(fruits_basket) 
print('task 8.',result)  

# task 9
def square_even_numbers(numbers):
    """
    This function takes a list of numbers, filters out the even numbers, and returns a new list
    where each even number is squared. 
    """
    return [x **2 for x in numbers if x % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = square_even_numbers(numbers)
print(f'task 9. {result}')  #  [4, 16, 36, 64, 100]

# task 10
def guess_alien_color(game_color):
    """
    This function checks if the user guessed the alien color correctly.
    If the color is correct, the user earns 10 points, otherwise, they earn 5 points.
    """
    alien_color = 'green' 
    if game_color == alien_color:
      
        return "Great! You just earned 10 points."
    
    else:
        
        return "Great! You just earned 5 points."

result = guess_alien_color("red") 
print("task 10.", result)  

result = guess_alien_color("green")  
print("task 10.", result)  