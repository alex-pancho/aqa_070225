def func():
   pass


def reversed_string(string: str):
   result = string[::-1]
   print(f"Строка {string} навпаки стала: {result}")
   return result




def sum_numbers_in_list(string_list: list):
   """Повертає список сум чисел зі списку строк,
  які складаються з чисел, розділених комою."""


   if not isinstance(string_list, list):
       raise ValueError("ValueError")


   if not string_list:
       raise ValueError("ValueError")


   result = []
   for item in string_list:
       try:
           if not isinstance(item, str):
               raise AttributeError("AttributeError")


           numbers = map(int, item.split(","))
           result.append(sum(numbers))
       except ValueError:
           result.append("Не можу це зробити!")
       except AttributeError as e:
           result.append(f"Не можу це зробити! {e}")


   return result




def math_average(small_list: list):
   math_average_number = sum(small_list) / len(small_list)
   print(f"Середнє арифметичне small_list: {math_average_number}")






class Student:
   def __init__(self, first_name, last_name, age, avarage_point):
       if not isinstance(avarage_point, (int, float)):
           raise TypeError("Average point must be a number")
       if age <= 0:
           raise ValueError("Age must be a positive integer")
       self.first_name = first_name
       self.last_name = last_name
       self.age = age
       self.avarage_point = avarage_point


   def change_avarege(self, new_avarage_point):
       if not isinstance(new_avarage_point, (int, float)):
           raise TypeError("Average point must be a number")
       self.avarage_point = new_avarage_point


   def student_info(self):
       print(f"Ім’я студента: {self.first_name}")
       print(f"Прізвище студента: {self.last_name}")
       print(f"Вік студента: {self.age}")
       print(f"Середній бал студента: {self.avarage_point}")






if __name__ == "__main__":


   #
   # longest_word(["word", "tetiana", "1"])
   #
   # reversed_string("Hello")


   # alien_color(alient_color) # поверне Колір: blue! гравець заробив 5 балів.
   # alien_color(None)  # поверне Error color.


   # numbers =[1, 2, 3, 4, "іваіва", 6, 7, 8, 9, 10]
   # get_even_squares(numbers)  # викликаємо функцію і передаємо в агрумент список чисел numbers
   # math_average([])
   # sum_numbers_in_list()
   # elements("hhh", True)
   # longest_word(454)
   math_average ([1, 2, 3, 4, "іваіва", 6, 7, 8, 9, 10])

